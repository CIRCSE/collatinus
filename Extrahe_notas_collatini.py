# -*- encoding: utf-8 -*-

#Sistema quel casino approssimativo che è (un output di) Collatinus

import codecs, sys

try :
	tagué = sys.argv[1]
	tagghi = sys.argv[2]
except (IndexError) :
	print("Inserire sia l'indirizzo dell'input che dell'output!")
	quit()

veteroindice = 0 #Serve per considerare solo la prima di alcune righe ripetute (perchè vengono ripetute?!)

with codecs.open(tagué,'r','utf8') as dentro :
	with codecs.open(tagghi,'w','utf8') as fuori :
	
		for riga in dentro :
		
			try :
				index,_,_,toko,posso,lemmata,_,_,_,_ = riga.strip().split('\t')
			except (ValueError) : #Per le righe unknown
				index,_,_,toko,posso,lemmata = riga.strip().split('\t')
			
			
			if index == veteroindice : #Salta le righe ripetute
				continue
			else : 
				veteroindice = index
			
			
			posso = posso.split(' ')[0] #Talvolta viene fornita anche un'intepretazione secondaria per la POS; consideriamo solo la prima
			
			#Modificare qua per stampare più o meno righe, o modificarne il formato
			#Potremmo decidere di inserire un pos per la punteggiatura, e anche la punteggiatura stessa come lemma
			fuori.write("%s\t%s\t%s\n" % (toko,posso,lemmata.replace(' ','')))
			
		
			###
			#Variante per stampare una singola colonna nel formato lem/pos,lem/pos,... (per ogni riga, il pos è uguale per tutti i lemmi) 
			#taggati = [lem+'/'+posso for lem in lemmata.split(', ')]
			#fuori.write('%s\n' % (','.join(taggati))) 
			