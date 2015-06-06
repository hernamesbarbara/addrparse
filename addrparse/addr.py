#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""addr.py
"""
from flanker.addresslib import address

WEBMAIL_HOSTS = [
    "gmail.com",
    "gmail.fr",
    "aol.com",
    "yahoo.com",
    "yahoo.fr",
    "me.com",
    "outlook.com",
    "comcast.net",
]

def validate_email(txt):
    if isinstance(txt, address.EmailAddress):
        return txt
    email = address.parse(txt)
    if address.is_email(email.address):
        return email
    else:
        return None

def is_webmail(email):
    email = validate_email(email)
    return any(email.hostname == pat for pat in WEBMAIL_HOSTS)

def guess_website(email):
    email = validate_email(email)
    if not email or is_webmail(email):
        return None
    else:
        return "http://www.{}".format(email.hostname)

def parse_mailbox(email):
    email = validate_email(email)
    if not email:
        return None
    return email.mailbox.title()

def get_name_list():
    return (l.strip().lower() for l in open('/usr/share/dict/propernames', 'r').readlines())

# NAMES = frozenset(["aaron", "adam", "adlai", "adrian", "agatha", "ahmed", "ahmet", "aimee", "al", "alain", "alan", "alastair", "albert", "alberto", "alejandro", "alex", "alexander", "alexis", "alf", "alfred", "alison", "allan", "allen", "alvin", "amanda", "amarth", "amedeo", "ami", "amigo", "amir", "amos", "amy", "anatole", "anatoly", "anderson", "andre", "andrea", "andreas", "andrew", "andries", "andy", "angela", "angus", "anita", "ann", "anna", "annard", "anne", "annie", "anthony", "anton", "antonella", "antonio", "antony", "archie", "ariel", "arlene", "arne", "arnold", "art", "arthur", "audrey", "avery", "axel", "barbara", "barbra", "barney", "barrett", "barrio", "barry", "bart", "barton", "bea", "beckie", "becky", "belinda", "ben", "benjamin", "benson", "bernard", "bernie", "bert", "bertrand", "beth", "betsy", "betty", "beverly", "bill", "billie", "billy", "bjorne", "blaine", "blair", "blake", "blayne", "bob", "bobbie", "bobby", "bonnie", "boyce", "boyd", "brad", "bradford", "bradley", "brandi", "brandon", "brandy", "brenda", "brendan", "brender", "brent", "bret", "brett", "brian", "briggs", "brodie", "brooke", "bruce", "bruno", "bryan", "bryce", "bucky", "bud", "butler", "byron", "caleb", "calvin", "carisa", "carl", "carlo", "carlos", "carol", "carole", "caroline", "carolyn", "carsten", "carter", "cary", "case", "casey", "casper", "catherine", "cathrin", "cathryn", "cathy", "cecilia", "celeste", "celia", "charleen", "charlene", "charles", "charley", "charlie", "chet", "chip", "chris", "christian", "christie", "christina", "christofer", "christophe", "christopher", "chuck", "cindie", "cindy", "claire", "clara", "clare", "clarence", "clarissa", "clark", "claude", "claudia", "claudio", "clay", "clayton", "clem", "cliff", "clifford", "clyde", "cole", "coleen", "colin", "collin", "connie", "conrad", "corey", "cory", "courtney", "craig", "cris", "cristi", "cristina", "cristopher", "curt", "curtis", "cynthia", "cyrus", "dale", "dalton", "damon", "damone", "dan", "dana", "dani", "daniel", "daniele", "danielle", "dannie", "danny", "darci", "daren", "darin", "darrell", "darren", "darryl", "daryl", "dave", "david", "dawn", "dawson", "dean", "deb", "debbie", "debi", "deborah", "deirdre", "del", "delbert", "denis", "dennis", "derek", "devon", "dewey", "diana", "diane", "dick", "dieter", "dimetry", "dimitry", "dion", "dirk", "dominic", "dominick", "don", "donal", "donald", "donn", "donna", "donne", "donnie", "donovan", "dori", "dorian", "dorothy", "dory", "doug", "douglas", "doyle", "drew", "duane", "duke", "duncan", "dustin", "dwayne", "dwight", "dylan", "earl", "earle", "earnie", "ed", "eddie", "eddy", "edgar", "edith", "edmond", "edmund", "eduardo", "edward", "edwin", "eileen", "elaine", "eli", "elias", "elijah", "eliot", "elisabeth", "elizabeth", "ellen", "elliot", "elliott", "elric", "elsa", "elvis", "elwood", "emil", "emily", "emma", "emmett", "eric", "erick", "erik", "ernest", "ernie", "ernst", "erwin", "ethan", "eugene", "eva", "evan", "evelyn", "everett", "farouk", "fay", "felix", "fletcher", "floria", "florian", "floyd", "frances", "francis", "francisco", "francois", "frank", "franklin", "fred", "frederic", "frederick", "fritz", "gabriel", "gail", "gale", "galen", "gary", "gene", "geoff", "geoffrey", "george", "gerald", "gerard", "gideon", "gigi", "gil", "giles", "gill", "gilles", "ginny", "giovanni", "glen", "glenn", "glynn", "gordon", "grace", "graeme", "graham", "grant", "granville", "greg", "gregg", "gregge", "gregor", "gregory", "gretchen", "griff", "guido", "guillermo", "gunnar", "gunter", "guy", "gypsy", "hal", "hamilton", "hank", "hans", "harmon", "harold", "harris", "harry", "hartmann", "harv", "harvey", "hazel", "heather", "hector", "heidi", "hein", "heinrich", "heinz", "helen", "helge", "henry", "herb", "herbert", "herman", "herve", "hienz", "hilda", "hillary", "hillel", "himawan", "hirofumi", "hirotoshi", "hiroyuki", "hitoshi", "hohn", "holly", "hon", "honzo", "horst", "hotta", "howard", "hsi", "hsuan", "huashi", "hubert", "huey", "hugh", "hughes", "hui", "hume", "hunter", "hurf", "hwa", "hy", "ian", "ilya", "ima", "indra", "ira", "irfan", "irvin", "irving", "irwin", "isaac", "isabelle", "isidore", "israel", "izchak", "izumi", "izzy", "jack", "jackye", "jacob", "jacobson", "jacques", "jagath", "jaime", "jakob", "james", "jamie", "jan", "jane", "janet", "janice", "janos", "jared", "jarl", "jarmo", "jarvis", "jason", "jay", "jayant", "jayesh", "jean", "jean-christophe", "jean-pierre", "jeanette", "jeanne", "jeannette", "jeannie", "jeany", "jef", "jeff", "jeffery", "jeffie", "jeffrey", "jelske", "jem", "jenine", "jennie", "jennifer", "jerald", "jeremy", "jerome", "jerrie", "jerry", "jesper", "jess", "jesse", "jesus", "ji", "jianyun", "jill", "jim", "jimmy", "jin", "jinchao", "jingbai", "jinny", "jiri", "jisheng", "jitendra", "joachim", "joanne", "jochen", "jock", "joe", "joel", "johan", "johann", "john", "johnathan", "johnnie", "johnny", "jon", "jonathan", "jones", "jong", "joni", "joon", "jordan", "jorge", "jos", "jose", "joseph", "josh", "joshua", "josip", "joubert", "joyce", "juan", "judge", "judith", "judy", "juergen", "juha", "julia", "julian", "juliane", "julianto", "julie", "juliet", "julius", "jun", "june", "jurevis", "juri", "jussi", "justin", "jwahar", "kaj", "kamel", "kamiya", "kanthan", "karen", "kari", "karl", "kate", "kathleen", "kathryn", "kathy", "kay", "kayvan", "kazuhiro", "kee", "kees", "keith", "kelly", "kelvin", "kemal", "ken", "kenn", "kenneth", "kent", "kenton", "kerri", "kerry", "kevan", "kevin", "kevyn", "kieran", "kiki", "kikki", "kim", "kimberly", "kimmo", "kinch", "king", "kirk", "kirsten", "kit", "kitty", "klaudia", "klaus", "knapper", "knudsen", "knut", "knute", "kolkka", "konrad", "konstantinos", "kory", "kris", "kristen", "kristi", "kristian", "kristin", "kriton", "krzysztof", "kuldip", "kurt", "kusum", "kyle", "kylo", "kyu", "kyung", "lana", "lance", "lanny", "lar", "larry", "lars", "laura", "laurel", "laurence", "laurent", "laurianne", "laurie", "lawrence", "lea", "leads", "lee", "leif", "leigh", "leila", "leith", "len", "lenny", "lenora", "leo", "leon", "leonard", "leora", "les", "leslie", "lester", "leung", "lewis", "lex", "liber", "lievaart", "lila", "lin", "linda", "linder", "lindsay", "lindsey", "linley", "lisa", "list", "liyuan", "liz", "liza", "lloyd", "lois", "lonhyn", "lord", "loren", "lorenzo", "lori", "lorien", "lorraine", "lou", "louie", "louiqa", "louis", "louise", "loukas", "lowell", "loyd", "luc", "lucifer", "lucius", "lui", "luis", "lukas", "luke", "lum", "lyndon", "lynn", "lynne", "lynnette", "maarten", "mac", "magnus", "mah", "mahesh", "mahmoud", "major", "malaclypse", "malcolm", "malloy", "malus", "manavendra", "manjeri", "mann", "manny", "manolis", "manuel", "mara", "marc", "marcel", "marci", "marcia", "marco", "marcos", "marek", "margaret", "margie", "margot", "marguerite", "maria", "marian", "marie", "marilyn", "mario", "marion", "mariou", "mark", "markus", "marla", "marlena", "marnix", "marsh", "marsha", "marshall", "martha", "martin", "marty", "martyn", "marvin", "mary", "masanao", "masanobu", "mason", "mat", "mats", "matt", "matthew", "matthias", "matthieu", "matti", "maureen", "maurice", "max", "mayo", "mechael", "meehan", "meeks", "mehrdad", "melinda", "merat", "merril", "merton", "metin", "micah", "michael", "micheal", "michel", "michelle", "michiel", "mick", "mickey", "micky", "miek", "mikael", "mike", "mikey", "miki", "miles", "milner", "milo", "miltos", "miriam", "miriamne", "mitch", "mitchell", "moe", "mohammad", "molly", "mongo", "monica", "monty", "moore", "moran", "morgan", "morris", "morton", "moses", "mosur", "mott", "murat", "murph", "murray", "murthy", "mwa", "myrick", "myron", "mysore", "nadeem", "naim", "nancy", "nanda", "naomi", "naoto", "naren", "narendra", "naresh", "nate", "nathan", "nathaniel", "natraj", "neal", "ned", "neil", "nelken", "neville", "nguyen", "nhan", "niall", "nichael", "nicholas", "nici", "nick", "nicolas", "nicolette", "nicolo", "niels", "nigel", "nikolai", "nils", "ning", "ninja", "no", "noam", "noemi", "nora", "norbert", "norm", "norma", "norman", "nou", "novo", "novorolsky", "ofer", "olaf", "old", "ole", "oleg", "oliver", "olivier", "olof", "olson", "omar", "orville", "oscar", "oskar", "owen", "ozan", "pablo", "page", "pam", "pamela", "panacea", "pandora", "panos", "pantelis", "panzer", "paola", "part", "pascal", "pat", "patrice", "patricia", "patricio", "patrick", "patty", "paul", "paula", "pedro", "peggy", "penny", "per", "perry", "pete", "peter", "petr", "phil", "philip", "philippe", "phill", "phillip", "phiroze", "pia", "piercarlo", "pierce", "pierette", "pierre", "piet", "piete", "pieter", "pilar", "pilot", "pim", "ping", "piotr", "pitawas", "plastic", "po", "polly", "pontus", "pradeep", "prakash", "pratap", "pratapwant", "pratt", "pravin", "presley", "pria", "price", "raanan", "rabin", "radek", "rafael", "rafik", "raghu", "ragnar", "rahul", "raif", "rainer", "raj", "raja", "rajarshi", "rajeev", "rajendra", "rajesh", "rajiv", "rakhal", "ralf", "ralph", "ram", "ramadoss", "raman", "ramanan", "ramesh", "ramiro", "ramneek", "ramon", "ramsey", "rand", "randal", "randall", "randell", "randolph", "randy", "ranjit", "raphael", "rathnakumar", "raul", "ravi", "ravindran", "ravindranath", "ray", "rayan", "raymond", "real", "rebecca", "rees", "reid", "reiner", "reinhard", "renu", "revised", "rex", "rhonda", "ric", "ricardo", "rich", "richard", "rick", "ricky", "rik", "ritalynne", "ritchey", "ro", "rob", "robbin", "robert", "roberta", "roberto", "robin", "rod", "rodent", "roderick", "rodger", "rodney", "roger", "rogue", "roland", "rolf", "rolfe", "romain", "roman", "ron", "ronald", "ronni", "root", "ross", "roxana", "roxane", "roxanne", "roxie", "roy", "rudolf", "rudolph", "rudy", "rupert", "russ", "russell", "rusty", "ruth", "saad", "sabrina", "saify", "saiid", "sal", "sally", "sam", "samir", "samuel", "sanand", "sanche", "sandeep", "sandip", "sandra", "sandy", "sanford", "sangho", "sanity", "sanjay", "sanjeev", "sanjib", "santa", "saqib", "sarah", "sassan", "saul", "saumya", "scot", "scott", "sean", "sedat", "sedovic", "seenu", "sehyo", "sekar", "serdar", "sergeant", "sergei", "sergio", "sergiu", "seth", "seymour", "shadow", "shahid", "shai", "shakil", "shamim", "shane", "shankar", "shannon", "sharada", "sharan", "shari", "sharon", "shatter", "shaw", "shawn", "shean", "sheila", "shel", "sherman", "sherri", "shirley", "sho", "shutoku", "shuvra", "shyam", "sid", "sidney", "siegurd", "sigurd", "simon", "siping", "sir", "sjaak", "sjouke", "skeeter", "skef", "skip", "slartibartfast", "socorrito", "sofia", "sofoklis", "son", "sonja", "sonny", "soohong", "sorrel", "space", "spass", "spencer", "spike", "spock", "spudboy", "spy", "spyros", "sri", "sridhar", "sridharan", "srikanth", "srinivas", "srinivasan", "sriram", "srivatsan", "ssi", "stacey", "stacy", "stagger", "stan", "stanislaw", "stanley", "stanly", "starbuck", "steen", "stefan", "stephan", "stephanie", "stephe", "stephen", "stevan", "steve", "steven", "stewart", "straka", "stu", "stuart", "subra", "sue", "sugih", "sumitro", "sundar", "sundaresan", "sunil", "suresh", "surya", "susan", "susanne", "susumu", "suu", "suwandi", "suyog", "suzan", "suzanne", "svante", "swamy", "syd", "syed", "sylvan", "syun", "tad", "tahsin", "tai", "tait", "takao", "takayuki", "takeuchi", "tal", "tammy", "tanaka", "tandy", "tanya", "tao", "tareq", "tarmi", "taurus", "ted", "teresa", "teri", "teriann", "terrance", "terrence", "terri", "terry", "teruyuki", "thad", "tharen", "the", "theo", "theodore", "thierry", "think", "thomas", "those", "thuan", "ti", "tiefenthal", "tigger", "tim", "timo", "timothy", "tobias", "toby", "todd", "toerless", "toft", "tolerant", "tollefsen", "tom", "tomas", "tommy", "tony", "tor", "torsten", "toufic", "tovah", "tracey", "tracy", "tran", "travis", "trent", "trevor", "trey", "triantaphyllos", "tricia", "troy", "trying", "tuan", "tuna", "turkeer", "tyler", "uri", "urs", "vadim", "val", "valentin", "valeria", "valerie", "van", "vance", "varda", "vassos", "vaughn", "venkata", "vern", "vernon", "vic", "vice", "vick", "vicki", "vickie", "vicky", "victor", "victoria", "vidhyanath", "vijay", "vilhelm", "vince", "vincent", "vincenzo", "vinod", "vishal", "vistlik", "vivek", "vladimir", "vladislav", "wade", "walt", "walter", "warren", "wayne", "wendell", "wendi", "wendy", "werner", "wes", "will", "william", "willie", "wilmer", "wilson", "win", "winnie", "winston", "wolf", "wolfgang", "woody", "yvonne"])

def process_email_address(txt):
    res = {
        "email": None, 
        "display_name": None, 
        "validated": None, 
        "iswebmail": None, 
        "outfile": None, 
        "mailbox": None, 
        "website": None, 
        "raw_input": None
    }
    res["raw_input"] = txt
    res['email'] = validate_email(res["raw_input"])
    res['validated'] = True if res['email'] else False

    if res.get('validated'):
        if res['email'].display_name:
            res['display_name'] = res['email'].display_name.title()
        res['iswebmail'] = is_webmail(res['email'])
        res['website'] = guess_website(res['email'])
        res['mailbox'] = parse_mailbox(res['email'])
    res = {k: None if v is None else str(v) for k, v in res.items()}
    return res
