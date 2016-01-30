flashProblems = [
    # working
[["My name is John.", 	"John"],
 ["My name is Bill.", 	"Bill"],
 ["My name is May.", 	"May"],
 ["My name is Mary.", 	"Mary"],
 ["My name is Josh.", 	"Josh"]],
    # working
[["james", 	"james."],
 ["charles", 	"charles."],
 ["thomas", 	"thomas."],
 ["paul", 	"paul."],
 ["chris", 	"chris."]],
    # working
[["don steve g.","dsg"],
 ["Kevin Jason Mat","KJM"],
 ["Jose Larry S","JLS"],
 ["Arthur Joe Juan","AJJ"],
 ["Raymond F. Timothy","RFT"]],
    # working
[["brent.hard@ho","brent hard"],
 ["matt.ra@yaho","matt ra"],
 ["jim.james@har","jim james"],
 ["ruby.clint@g","ruby clint"],
 ["josh.smith@g","josh smith"]],
# working    
[["John DOE 3 Data [TS]865-000-0000 - - 453442-00 06-23-2009","865-000-0000"],
 ["A FF MARILYN 30'S 865-000-0030 - 4535871-00 07-07-2009","865-000-0030"],
 ["A GEDA-MARY 100MG 865-001-0020 - - 5941-00 06-23-2009","865-001-0020"],
 ["Sue DME 42 [ST]865-003-0100 -- 5555-99 08-22-2010","865-003-0100"],
 ["Edna DEECS [SSID] 865-001-0003 --23954-11 09-01-2010","865-001-0003"]],
# working
[["Company\\\\Code\\\\index.html","Company\\\\Code\\\\"],
 ["Company\\\\Docs\\\\Spec\\\\specs.doc","Company\\\\Docs\\\\Spec\\\\"],
 ["Work\\\\Presentations\\\\talk.ppt","Work\\\\Presentations\\\\"],
 ["Work\\\\Records\\\\2010\\\\January.dat","Work\\\\Records\\\\2010\\\\"],
 ["Proj\\\\Numerical\\\\Simulators\\\\NBody\\\\nbody.c","Proj\\\\Numerical\\\\Simulators\\\\NBody\\\\"]],
    # an example of ambiguity
[["hi","hi hi"],
 ["bye","hi bye"],
 ["adios","hi adios"],
 ["joe","hi joe"],
 ["icml","hi icml"]],
    # working
[["Oege de Moor","Oege de Moor"],
 ["Kathleen Fisher AT&T Labs","Kathleen Fisher AT&T Labs"],
 ["Microsoft Research","Microsoft Research"],
 ["John Morse Institute","John Morse Institute"],
 ["Jennifer Smith Law Firm","Jennifer Smith Law Firm"]],
    # working
[["1/21/2001","01"],
 ["22.02.2002","02"],
 ["2003-23-03","03"],
 ["21/1/2001","01"],
 ["5/5/1987","87"]],
    # working
[["Eyal Dechter","Dechter, Eyal"],
 ["Joshua B. Tenenbaum","Tenenbaum, Joshua B."],
 ["Stephen H. Muggleton","Muggleton, Stephen H."],
 ["Kevin Ellis","Ellis, Kevin"],
 ["Dianhuan Lin","Lin, Dianhuan"]],
    # working
[["12/31/13","12.31"],
 ["1/23/2009","1.23"],
 ["4/12/2023","4.12"],
 ["6/23/15","6.23"],
 ["7/15/2015","7.15"]],
    # not working and I don't understand why
[["Three <2: vincent> Jeff","(2: vincent)"],
 ["Don Kyle <3: ricky> virgil","(3: ricky)"],
 ["herbert is <2: marion> morris","(2: marion)"],
 ["fransisco eduardo <1: apple trees>","(1: apple trees)"],
 ["country music <9: refrigerator>","(9: refrigerator)"]],
    # working, but slow
[["3113 Greenfield Ave., Los Angeles, CA 90034","Los Angeles"],
 ["43 St. Margaret St. #1, Dorchester, MA 02125","Dorchester"],
 ["43 Vassar St. 46-4053, Cambridge, MA 02139","Cambridge"],
 ["47 Foskett St. #2, Cambridge, MA 02144","Cambridge"],
 ["3 Ames St., Portland, OR 02142","Portland"]],
    # working
[["Verlene Ottley  ","V.O"],
 ["Oma Cornelison  ","O.C"],
 ["Marin Lorentzen  ","M.L"],
 ["Annita Nicely  ","A.N"],
 ["Joanie Faas  ","J.F"]],
    # working
[["Agripina Kuehner  ","Hi Agripina!"],
 ["Brittany Alarcon  ","Hi Brittany!"],
 ["Adelia Swindell  ","Hi Adelia!"],
 ["Marcie Michalak  ","Hi Marcie!"],
 ["Eugena Eurich  ","Hi Eugena!"]],
    # working
[["#include <stdio.h>","stdio"],
 ["#include <malloc.h>","malloc"],
 ["#include <stdlib.h>","stdlib"],
 ["#include <sys.h>","sys"],
 ["#include <os.h>","os"]],
    # working
[["aa",	   "aaa"],
 ["abc",	   "abcc"],
 ["xyz",	   "xyzz"],
 ["4",	   "44"],
 ["john",   "johnn"]],
    # working with the large array bounds
[["3113 Greenfield Ave., LA, CA 90034",	"3113"],
 ["43 St. Margaret St. #1, Dorchester, MA 02125","43"],
 ["43 Vassar St. 46-4053, Cambridge, MA 02139",	"43"],
 ["47 Foskett St. #2, Cambridge, MA 02144",	"47"],
 ["3 Ames St., Portland, OR 02142", 		"3"]],
    # working
[["aa",	   "aaaa"],
 ["abc",	   "abcabc"],
 ["xyz",	   "xyzxyz"],
 ["4",	   "44"],
 ["john",   "johnjohn"]]
]
