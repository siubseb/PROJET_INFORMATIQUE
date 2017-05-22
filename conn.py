# -*- coding: utf-8 -*-

import socket
import random
import time


def cls():
    print "\n" * 100

connexonEtablie = False
validIP = False

type_conn = ""
while type_conn != "H" and type_conn != "C":
        type_conn = raw_input("Veuillez selectionner [H]ote ou [C]lient : ").upper()


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
localIP = s.getsockname()[0]

if type_conn == "H":    #HOTE

        def inGameCls():
            print "\n" * 100
            print "Vous êtes actuellement en jeu avec " + str(info_client[0])
            print "_" * 5
            print ""
 
        print ""
        print "Une partie est hebergée sur " + str(localIP) + ":120 ..."
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("", 120))
        server.listen(5)
		
		
        print "attente d'un joueur..."
        print
        connexionClient, info_client = server.accept()
        cls()
        print "{} s'est connecté".format( info_client )
        connexionClient.send(b"syncFromHostOK")
        print
        print "attente du client ..."

        data = connexionClient.recv(1024).decode()

        if data == "syncFromClientOK":
            cls()
            print "Connexion etablie, la partie va commencer sous peu.."
            connexionClient.close()
            time.sleep(3)
            inGameCls()
            raw_input("test")
                

if type_conn == "C":    #Client


        def inGameCls():
            print "\n" * 100
            print "Vous êtes actuellement en jeu avec " + host
            print "_" * 5
            print ""

        waitMessage = 0
        
        connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                  
        while validIP == False:
            print ""
            host = raw_input("Veuillez entrer l'adresse IP de l'hote : ").lower()
            try:
                socket.inet_aton(host)
                validIP = True
                print ""
            except socket.error:
                validIP = False
                print "L'adresse IP est invalide."

        s.close()
        connexion.connect((host, 120))
        print "connecte, synchronisation..."
        print
        data = connexion.recv(1024).decode()
        print ""
        print "attente de l'hôte ..."
        if data == "syncFromHostOK":
            print
            connexion.send(b"syncFromClientOK")
            cls()
            print "Connexion etablie, la partie va commencer sous peu.."
            connexion.close()
            time.sleep(3)
            
            inGameCls()
            raw_input("test")
