from gettext import gettext as _

PER_100_GRAMS = ["kcal","protein","lipid","ash","carb","fiber","sugar","calcium","iron","magnesium","phosphorus","potassium","sodium","zinc","copper","manganese","selenium","vitaminc","thiamin","riboflavin","niacin","pantoacid","vitaminb6","folatetotal","folateacid","foodfolate","folatedfe","vitb12","vitaiu","vitarae","retinol","vite","vitk","alphac","betac","betacrypt","lypocene","famono","fapoly","lutzea","fasat","cholestrl"]

NUTRITION_FIELDS = [
    #[description abbrev type]
    ["Nutrient Databank Number","ndbno","int"],
    ["Short Description","desc","char(100)"],
    [_("Water"),"water","float"],    
    [_("Kilocalories"),"kcal","float"],
    [_("g protein"),"protein","float"],
    [_("g lipid"),"lipid","float"],
    [_("g ash"),"ash","float"],
    [_("g carbohydrates"),"carb","float"],
    [_("g fiber"),"fiber","float"],
    [_("g sugar"),"sugar","float"],
    [_("mg calcium"),"calcium","float"],
    [_("mg iron"),"iron","float"],
    [_("mg magnesium"),"magnesium","float"],
    [_("mg phosphorus"),"phosphorus","float"],
    [_("mg potassium"),"potassium","float"],
    [_("mg sodium"),"sodium","float"],
    [_("mg zinc"),"zinc","float"],
    [_("mg copper"),"copper","float"],
    [_("mg manganese"),"manganese","float"],
    [_("microgram selenium"),"selenium","float"],
    [_("mg vitamin c"),"vitaminc","float"],
    [_("mg thiamin"),"thiamin","float"],
    [_("mg riboflavin"),"riboflavin","float"],
    [_("mg niacin"),"niacin","float"],
    [_("mg pantothenic acid"),"pantoacid","float"],
    [_("mg vitamin B6"),"vitaminb6","float"],
    [_("microgram Folate Total"),"folatetotal","float"],
    [_("microgram Folic acid"),"folateacid","float"],
    [_("microgram Food Folate"),"foodfolate","float"],
    [_("microgram dietary folate equivalents"),"folatedfe","float"],
    [_("microgram Vitamin B12"),"vitb12","float"],
    [_("Vitamin A IU"),"vitaiu","float"],
    [_("Vitamin A (microgram Retinal Activity Equivalents"),"vitarae","float"],
    [_("microgram Retinol"),"retinol","float"],
    [_("mg Vitamin E"),"vite","float"],
    [_("mg Vitamin K"),"vitk","float"],
    [_("microgram Alpha-carotene"),"alphac","float"],
    [_("microgram Beta-carotene"),"betac","float"],
    [_("microgram Beta Cryptoxanthin"),"betacrypt","float"],
    [_("microgram Lycopene"),"lypocene","float"],
    [_("microgram Lutein+Zeazanthin"),"lutzea","float"],
    [_("g Saturated Fatty Acid"),"fasat","float"],
    [_("g Monounsaturated Fatty Acids"),"famono","float"],
    [_("g Polyunsaturated Fatty Acids"),"fapoly","float"],
    [_("mg Cholesterol"),"cholestrl","float"],
    ["Gram Weight 1","gramwt1","float"],
    ["Gram Weight Description 1","gramdsc1","char(100)"],
    ["Gram Weight 2","gramwt2","float"],
    ["Gram Weight Description 2","gramdsc2","char(100)"],
    [_("Percent refuse"),"refusepct","float"],
    ]

# List of fields that can be sensibly added, multiplied, etc.
SUMMABLE_FIELDS = ['kcal','protein','lipid','carb',
                   'fiber','calcium','magnesium','potassium',
                   'sodium','copper','vitaminc','riboflavin','pantoacid',
                   'vitaminb6','folateacid','folatedfe','vitaiu',
                   'vitarae','vite','alphac','betacrypt','lutzea','famono',
                   'fapoly',]

# a convenient dictionary to move from shortname to longname,
# for user interface.
NUT_FIELDNAME_DICT = {}
for longname,sname,field in NUTRITION_FIELDS:
    NUT_FIELDNAME_DICT[sname]=longname

ABBREVS = {'ALLPURP':'All Purpose',
           'AL':'Aluminum',
           '&':'And',
           'APPL':'Apple',
           'APPLS':'Apples',
           'APPLSAUC':'Applesauce',
           'APPROX':'Approximate',
           'APPROX':'Approximately',
           'ARM&BLD':'Arm and Blade',
           'ARM And BLD':'Arm and Blade',
           'ART':'Artificial',
           'VIT C':'Ascorbic Acid',
           'ASPRT':'Aspartame',
           'ASPRT-SWTND':'Aspartame-sweetened',
           'BABYFD':'Babyfood',
           'BKD':'Baked',
           'BBQ':'Barbequed',
           'BSD':'Based',
           'BNS':'Beans',
           'BF':'Beef',
           'BEV':'Beverage',
           'BLD':'Boiled',
           'BNLESS':'Boneless',
           'BTLD':'Bottled',
           'BTTM':'Bottom',
           'BRSD':'Braised',
           'BRKFST':'Breakfast',
           'BRLD':'Broiled',
           'BTTRMLK':'Buttermilk',
           'CA':'Calcium',
           'CAL':'Calorie, calories',
           'CND':'Canned',
           'CARB':'Carbonated',
           'CNTR':'Center',
           'CRL':'Cereal',
           'CHS':'Cheese',
           'CHICK':'Chicken',
           'CHOC':'Chocolate',
           'CHOIC':'Choice',
           'CHOL':'Cholesterol',
           'CHOL-FREE':'Cholesterol-free',
           'CHOPD':'Chopped',
           'CINN':'Cinnamon',
           'COATD':'Coated',
           'COCNT':'Coconut',
           'COMM':'Commercial',
           'COMMLY':'Commercially',
           'CMDTY':'Commodity',
           'COMP':'Composite',
           'CONC':'Concentrate',
           'CONCD':'Concentrated',
           'COND':'Condensed',
           'CONDMNT':'Condiment, condiments',
           'CKD':'Cooked',
           'CTTNSD':'Cottonseed',
           'CRM':'Cream',
           'CRMD':'Creamed',
           'DK':'Dark',
           'DECORT':'Decorticated',
           'DEHYD':'Dehydrated',
           'DSSRT':'Dessert, desserts',
           'DIL':'Diluted',
           'DOM':'Domestic',
           'DRND':'Drained',
           'DRSNG':'Dressing',
           'DRK':'Drink',
           'DRUMSTK':'Drumstick',
           'ENG':'English',
           'ENR':'Enriched',
           'EQ':'Equal',
           'EVAP':'Evaporated',
           'XCPT':'Except',
           'EX':'Extra',
           'FLANKSTK':'Flank steak',
           'FLAV':'Flavored',
           'FLR':'Flour',
           'FD':'Food',
           'FORT':'Fortified',
           'FRENCH FR':'French fried',
           'FRENCH FR':'French fries',
           'FRSH':'Fresh',
           'FRSTD':'Frosted',
           'FRSTNG':'Frosting',
           'FRZ':'Frozen',
           'GRDS':'Grades',
           'GM':'Gram',
           'GRN':'Green',
           'GRNS':'Greens',
           'HTD':'Heated',
           'HVY':'Heavy',
           'HI-MT':'Hi-meat',
           'HI':'High',
           'HR':'Hour',
           'HYDR':'Hydrogenated',
           'IMITN':'Imitation',
           'IMMAT':'Immature',
           'IMP':'Imported',
           'INCL':'Include, includes',
           'INCL':'Including',
           'INF FORMULA':'Infant formula',
           'ING':'Ingredient',
           'INST':'Instant',
           'JUC':'Juice',
           'JR':'Junior',
           'KRNLS':'Kernels',
           'LRG':'Large',
           'LN':'Lean',
           'LN':'Lean only',
           'LVND':'Leavened',
           'LT':'Light',
           'LIQ':'Liquid',
           'LO':'Low',
           'LOFAT':'Low Fat',
           'MARSHMLLW':'Marshmallow',
           'MSHD':'Mashed',
           'MAYO':'Mayonnaise',
           'MED':'Medium',
           'MESQ':'Mesquite',
           'MIN':'Minutes',
           'MXD':'Mixed',
           'MOIST':'Moisture',
           'NAT':'Natural',
           'NZ':'New Zealand',
           'NFDM':'Nonfat Dry Milk',
           'NFDMS':'Nonfat Dry Milk Solids',
           'NFMS':'Nonfat Milk Solids',
           'NONCARB':'Noncarbonated',
           'NFS':'Not Further Specified',
           'NUTR':'Nutrients',
           'NUTR':'Nutrition',
           'OZ':'Ounce',
           'PK':'Pack',
           'PAR FR':'Par fried',
           'PARBLD':'Parboiled',
           'PART':'Partial',
           'PART':'Partially',
           'PAR FR':'Partially fried',
           'PAST':'Pasteurized',
           'PNUT':'Peanut',
           'PNUTS':'Peanuts',
           'PO4':'Phosphate',
           'P':'Phosphorus',
           'PNAPPL':'Pineapple',
           'PLN':'Plain',
           'PRTRHS':'Porterhouse',
           'K':'Potassium',
           'PDR':'Powder',
           'PDR':'Powdered',
           'PRECKD':'Precooked',
           'PREHTD':'Preheated',
           'PREP':'Prepared',
           'PROC':'Processed',
           'PROD CD':'Product code',
           'PROP':'Propionate',
           'PROT':'Protein',
           'PUDD':'Pudding, puddings',
           'RTB':'Ready-to-bake',
           'RTC':'Ready-to-cook',
           'RTD':'Ready-to-drink',
           'RTE':'Ready-to-eat',
           'RTF':'Ready-to-feed',
           'RTH':'Ready-to-heat',
           'RTS':'Ready-to-serve',
           'RTU':'Ready-to-use',
           'RECON':'Reconstituted',
           'RED':'Reduced',
           'RED-CAL':'Reduced-calorie',
           'REFR':'Refrigerated',
           'REG':'Regular',
           'REHTD':'Reheated',
           'REPLCMNT':'Replacement',
           'REST-PREP':'Restaurant-prepared',
           'RTL':'Retail',
           'RST':'Roast',
           'RSTD':'Roasted',
           'RND':'Round',
           'SNDWCH':'Sandwich',
           'SAU':'Sauce',
           'SCALLPD':'Scalloped',
           'SCRMBLD':'Scrambled',
           'SD':'Seed',
           'SEL':'Select',
           'SHK&SIRL':'Shank and sirloin',
           'SHK And SIRL':'Shank and sirloin',           
           'SHRT':'Short',
           'SHLDR':'Shoulder',
           'SIMMRD':'Simmered',
           'SKN':'Skin',
           'SML':'Small',
           'NA':'Sodium',
           'SOL':'Solids',
           'SOLN':'Solution',
           'SOYBN':'Soybean',
           'SPL':'Special',
           'SP':'Species',
           'SPRD':'Spread',
           'STD':'Standard',
           'STMD':'Steamed',
           'STWD':'Stewed',
           'STK':'Stick',
           'STKS':'Sticks',
           'STR':'Strained',
           'SUB':'Substitute',
           'SMMR':'Summer',
           'SUPP':'Supplement',
           'SWT':'Sweet',
           'SWTND':'Sweetened',
           'SWTNR':'Sweetener',
           'TSP':'Teaspoon',
           '1000':'Thousand',
           'TSTD':'Toasted',
           'TODD':'Toddler',
           'UNCKD':'Uncooked',
           'UNCRMD':'Uncreamed',
           'UNDIL':'Undiluted',
           'UNENR':'Unenriched',
           'UNHTD':'Unheated',
           'UNPREP':'Unprepared',
           'UNSPEC':'Unspecified',
           'UNSWTND':'Unsweetened',
           'VAR':'Variety, varieties',
           'VEG':'Vegetable, vegetables',
           'VIT A':'Vitamin A',
           'VIT C':'Vitamin C',
           'H20':'Water',
           'WHTNR':'Whitener',
           'WHL':'Whole',
           'WNTR':'Winter',
           'YEL':'Yellow',}

ABBREVS_STRT = {'W/':'with ',
                'WO/':'without ',
                '&':' and ',
                }