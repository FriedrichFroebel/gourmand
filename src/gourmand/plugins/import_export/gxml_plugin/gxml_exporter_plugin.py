import re

from gourmand.convert import float_to_frac, seconds_to_timestring
from gourmand.i18n import _
from gourmand.plugin import ExporterPlugin

from . import gxml2_exporter

GXML = _("Gourmet XML File")


class GourmetExportChecker:

    def check_rec(self, rec, file):
        self.txt = file.read()
        print("txt", self.txt)
        self.rec = rec
        self.check_attrs()

    def check_attrs(self):
        for attr in ["title", "cuisine", "source", "link"]:
            if getattr(self.rec, attr):
                assert re.search(
                    r"<%(attr)s>\s*%(val)s\s*</%(attr)s>" % {"attr": attr, "val": getattr(self.rec, attr)}, self.txt
                ), "Did not find %s value %s" % (attr, getattr(self.rec, attr))
        if self.rec.yields:
            assert re.search(r"<yields>\s*%s\s*%s\s*</yields>" % (self.rec.yields, self.rec.yield_unit), self.txt) or re.search(
                r"<yields>\s*%s\s*%s\s*</yields>" % (float_to_frac(self.rec.yields), self.rec.yield_unit), self.txt
            ), "Did not find yields value %s %s" % (self.rec.yields, self.rec.yield_unit)
        for att in ["preptime", "cooktime"]:
            if getattr(self.rec, att):
                tstr = seconds_to_timestring(getattr(self.rec, att))
                assert re.search(r"<%(att)s>\s*%(tstr)s\s*</%(att)s>" % locals(), self.txt), "Did not find %s value %s" % (att, tstr)


class GourmetExporterPlugin(ExporterPlugin):

    label = _("Gourmet XML Export")
    sublabel = _("Exporting recipes to Gourmet XML file %(file)s.")
    single_completed_string = (_("Recipe saved in Gourmet XML file %(file)s."),)
    filetype_desc = GXML
    saveas_filters = [GXML, ["text/xml"], ["*.grmt", "*.xml", "*.XML"]]
    saveas_single_filters = saveas_filters

    def get_multiple_exporter(self, args):
        return gxml2_exporter.recipe_table_to_xml(
            args["rd"],
            args["rv"],
            args["file"],
        )

    def do_single_export(self, args):
        gxml2_exporter.recipe_table_to_xml(args["rd"], [args["rec"]], args["out"], change_units=args["change_units"], mult=args["mult"]).run()

    def run_extra_prefs_dialog(self):
        pass

    def check_export(self, rec, file):
        gec = GourmetExportChecker()
        gec.check_rec(rec, file)
