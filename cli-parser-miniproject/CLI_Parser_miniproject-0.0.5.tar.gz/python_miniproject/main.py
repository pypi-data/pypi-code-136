import sys
sys.path += ['/modules/helper','modules/parser','modules/plugins','modules/tests','modules/utility']
from modules.parser.cli import cli
from modules.helper.mid_format import Mid
from modules.parser.RegexParserUrl import RegexParserUrl
from modules.parser.regex import RegexParser
from modules.plugins.csv import CSV_Output
from modules.plugins.json import Json_Output


if __name__=='__main__':
    input_script=cli()
    args=input_script.get_arguments()
    print(args)

    if args.regex:
        #checking for valid regex,i/p and o/p format
        mid_format = Mid()
        if(args.url==None):
            obj = RegexParser(args)
        else:
            obj = RegexParserUrl(args)

        yielded_dic = obj.parse()
        for retv in yielded_dic:
            mid_format.list_of_dic.append(retv)
    
     #if regular expression matches with no line:
    if(len(mid_format.list_of_dic)==0):
        sys.exit('\033[1;31mGiven Regular Expression did not match with any line\nExiting...\033[00m')
    if args.json is False:
        #do csv route
        print('\033[1;33mStoring in CSV format\033[00m')
        op = CSV_Output(mid_format,args)
        op.write_txt()
    elif args.json is True:
        #do json route
        print('\033[1;33mStoring in JSON format\033[00m')
        op = Json_Output(mid_format,args)
        op.write_txt()
    #ANSI formatting for coloring
    print('\033[1;34m*\033[00m'*100)
