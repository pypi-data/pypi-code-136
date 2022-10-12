from time import  strftime
def methodA():
	print("method A OCDGRAPHYMAL executed")
	dt_string = strftime("%d_%m_%Y-%H_%M_%S")
	filename = "/tmp/ocdgraphy_methodA_1_"+dt_string+".txt" 
	f = open(filename, "w")
	f.write("COUCOU")
	f.close()
	