#****import****
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import base64
import json
from datetime import date
from error_recup import Form1
from recup_done import Form2
from verif import Form3
from E_personne import Form4
from ajout_eff import Form5
from enregistrement import Form6
from close import Form7
from test import MainWindow
import pickle as pk
# ****Création de dictionnaire****
dict_p = {'cin': '','nom': '', 'prenom': '', 'age': '','adresse': '', 'nationalite': '', 'tel': '', 'jr': '', 'ms': '', 'an': '', 'dcd': ''}
dict_m = {'code': '','cin': '', 'nom_m': '', 'nb': ''}
list_p=[]
list_m=[]


#****code****
class Ui(QtWidgets.QMainWindow):
    def recup_pers(self):
        global list_p
        with open(r"Personne.dat", "rb") as f:
            encoded_list=pk.load(f)
            decoded_list = base64.b64decode(encoded_list)
            list_p = json.loads(decoded_list.decode('utf-8'))
    def recup_mld(self):
        global list_m
        with open(r"Maladie.dat", "rb") as f:
            encoded_list=pk.load(f)
            decoded_list = base64.b64decode(encoded_list)
            list_m = json.loads(decoded_list.decode('utf-8'))

    def __init__(self):
        global rcp
        super(Ui,self).__init__()
        uic.loadUi('main.ui',self)
        rcp=False
        #Edits
        self.setWindowTitle("Application CORONA")
        self.setWindowIcon(QIcon("Source/infected.png"))
        self.center()
        self.widget_5.hide()
        self.widget_4.hide()
        self.widget_7.hide()
        self.widget_6.hide()
        self.widget_8.hide()
        self.widget_2.hide()
        self.widget_3.hide()
        self.widget_9.hide()
        self.widget_10.hide()
        self.widget_11.hide()
        self.listWidget_1.hide()
        self.listWidget_2.hide()
        self.listWidget_3.hide()
        self.listWidget_8.hide()
        self.listWidget_5.hide()
        self.listWidget_6.hide()
        self.comboBox_6.hide()
        self.comboBox_7.hide()
        self.comboBox_8.hide()
        self.pushButton.clicked.connect(self.menu)
        self.G_personnes.clicked.connect(self.pers)
        self.pushButton_2.clicked.connect(self.M_pers)
        self.G_maladie.clicked.connect(self.mal)
        self.pushButton_7.clicked.connect(self.M_mal)
        self.enreg.clicked.connect(self.Enr)
        #Button link
        self.ACCUEIL.clicked.connect(self.B1)
        self.pushButton_5.clicked.connect(self.B2)
        self.pushButton_6.clicked.connect(self.B3)
        self.pushButton_4.clicked.connect(self.B4)
        self.pushButton_3.clicked.connect(self.B5)

        self.pushButton_8.clicked.connect(self.B6)
        self.pushButton_9.clicked.connect(self.B7)
        self.pushButton_10.clicked.connect(self.B8)
        self.pushButton_11.clicked.connect(self.B9)
        self.calcul_affi.clicked.connect(self.B10)
        self.pushButton_34.clicked.connect(self.close)

        self.recup.clicked.connect(self.recup_done)

        self.radioButton_2.clicked.connect(self.sp_show)
        self.radioButton_3.clicked.connect(self.sp_show)
        self.radioButton_4.clicked.connect(self.sp_show)

        self.radioButton_5.clicked.connect(self.rch_aff)
        self.radioButton_6.clicked.connect(self.rch_aff)
        self.radioButton_7.clicked.connect(self.rch_aff)
        self.radioButton_8.clicked.connect(self.rch_aff)
        self.radioButton_9.clicked.connect(self.rch_aff)
        self.radioButton_10.clicked.connect(self.rch_aff)

        self.pushButton_16.clicked.connect(self.enregister_tt)
        self.pushButton_15.clicked.connect(self.enregister_maladie)
        self.pushButton_12.clicked.connect(self.enregister_personne)
        self.pushButton_17.clicked.connect(self.supprimer_personne)
        self.pushButton_22.clicked.connect(self.supprimer_maladie)
        self.pushButton_18.clicked.connect(self.modifier_personne)
        self.pushButton_23.clicked.connect(self.modifier_maladie)
        self.pushButton_19.clicked.connect(self.RA_personne)
        self.pushButton_20.clicked.connect(lambda:self.stackedWidget_3.setCurrentWidget(self.page_5))
        self.pushButton_25.clicked.connect(lambda:self.stackedWidget_3.setCurrentWidget(self.page_10))
        self.pushButton_26.clicked.connect(lambda:self.stackedWidget_3.setCurrentWidget(self.page_10))
        self.pushButton_28.clicked.connect(lambda:self.stackedWidget_3.setCurrentWidget(self.page_10))
        self.pushButton_29.clicked.connect(lambda:self.stackedWidget_3.setCurrentWidget(self.page_10))
        self.pushButton_31.clicked.connect(lambda:self.stackedWidget_3.setCurrentWidget(self.page_16))
        self.pushButton_32.clicked.connect(lambda:self.stackedWidget_3.setCurrentWidget(self.page_16))
        self.pushButton_27.clicked.connect(lambda:self.stackedWidget_3.setCurrentWidget(self.page_16))
        self.pushButton_33.clicked.connect(lambda:self.stackedWidget_3.setCurrentWidget(self.page_16))
        self.mini.clicked.connect(self.fullscreen)
        self.pushButton_30.clicked.connect(self.RA)
        self.pushButton_21.clicked.connect(self.ajout_m)
        self.pushButton_14.clicked.connect(self.ajout_p)
        self.pushButton_24.clicked.connect(self.RA_maladie)
        self.comboBox_3.currentIndexChanged.connect(self.change_item)
        self.comboBox_9.currentIndexChanged.connect(self.change_personne)

    def change_personne(self):
        self.comboBox_10.clear()
        nom=self.comboBox_9.currentText()
        self.comboBox_10.addItem("Tous Les Personnes")
        for i in list_m:
            if(self.comboBox_10.findText(i['cin'])==-1 and nom == i['nom_m']):
                self.comboBox_10.addItem(str(i['cin']))

    def change_item(self):
        self.comboBox_4.clear()
        cin=self.comboBox_3.currentText()
        for i in list_m:
            if(i['cin']==cin):
                self.comboBox_4.addItem(i['nom_m'])

    def closeEvent(self, event):
        confirmation = Form3()
        with open(r"Personne.dat", "rb") as f:
            encoded_list=pk.load(f)
            decoded_list = base64.b64decode(encoded_list)
            l1 = json.loads(decoded_list.decode('utf-8'))
        with open(r"Maladie.dat", "rb") as f:
            encoded_list=pk.load(f)
            decoded_list = base64.b64decode(encoded_list)
            l2 = json.loads(decoded_list.decode('utf-8'))

        if(l1==list_p and l2==list_m or rcp==False):
            event.accept()
        else:
            if confirmation.exec_() == QDialog.Accepted:
                event.accept()
            else:
                event.ignore()
                with open(r"Personne.dat", "wb") as f:
                    json_list = json.dumps(list_p)
                    encoded_list = base64.b64encode(json_list.encode('utf-8'))
                    pk.dump(encoded_list, f)
                with open(r"Maladie.dat", "wb") as f:
                    json_list = json.dumps(list_m)
                    encoded_list = base64.b64encode(json_list.encode('utf-8'))
                    pk.dump(encoded_list, f)
                self.er = Form7()
                self.er.show()
                QTimer.singleShot(1500, self.close)

    def fullscreen(self):
        if self.windowState() == Qt.WindowFullScreen:
            self.mini.setText("Full Screen Mode")
            self.mini.setIcon(QIcon("Source/full-size.png"))
            self.pushButton_34.hide()
            self.showNormal()
        else:
            self.mini.setText("Quitter Full Screen")
            self.mini.setIcon(QIcon("Source/minimize.png"))
            self.pushButton_34.show()
            self.showFullScreen()

    def RA(self):
        if (not self.radioButton_20.isChecked() and not self.radioButton_21.isChecked() and not self.radioButton_22.isChecked() and not self.radioButton_23.isChecked()):
            self.er=Form4()
            self.er.label.setText(" Choisir une option !")
            self.er.show()
        elif(self.radioButton_20.isChecked()):
            self.tableWidget_4.setRowCount(0)
            nat=self.comboBox_8.currentText()
            self.tableWidget_4.setColumnCount(11)
            if(nat==""):
                self.er=Form4()
                self.er.label.setText("Aucun element à Afficher !")
                self.er.show()
            else:
                l1=list()
                for i in list_p:
                    if(i['nationalite']==nat):
                        l1.append(i)

                self.tableWidget_4.setRowCount(len(l1))
                self.tableWidget_4.setColumnCount(11)
                for row in range(self.tableWidget_4.rowCount()):
                    col=0
                    for i in l1[row].values():
                        item = QTableWidgetItem(str(i))
                        self.tableWidget_4.setItem(row, col, item)
                        col+=1
                self.stackedWidget_3.setCurrentWidget(self.page_13)
        elif(self.radioButton_21.isChecked()):
            d1 = QDate.currentDate().day()
            m1 = QDate.currentDate().month()
            y1 = QDate.currentDate().year()
            while(self.listWidget.count() > 1):
                last_item_index = self.listWidget.count() - 1
                self.listWidget.takeItem(last_item_index)
            for i in list_p:
                d2=int(i['jr'])
                m2=int(i['ms'])
                y2=int(i['an'])
                date1 = date(y1, m1, d1)
                date2 = date(y2, m2, d2)
                delta = date1 - date2
                if(delta.days<=14):
                    self.listWidget.addItem(str(i['cin'])+" "+str(i['nom'])+" "+str(i['prenom']))
            self.stackedWidget_3.setCurrentWidget(self.page_17)
            if(self.listWidget.count()==1):
                self.er=Form4()
                self.er.label.setText("Aucun personne En quarantaine !")
                self.er.show()
        elif(self.radioButton_22.isChecked()):
            while(self.listWidget_17.count() > 2):
                last_item_index = self.listWidget_17.count() - 1
                self.listWidget_17.takeItem(last_item_index)
            nb=0
            for i in list_p:
                if(int(i['dcd'])==1):
                    nb+=1
                    self.listWidget_17.addItem(str(i['cin'])+" "+str(i['nom'])+" "+str(i['prenom']))
            self.stackedWidget_3.setCurrentWidget(self.page_18)
            if(self.listWidget_17.count()==1):
                item=self.listWidget_17.item(1)
                item.setText(  "*** Pourcentage De Décès: 0% ***")
                self.er=Form4()
                self.er.label.setText("Aucun personne Décédé !")
                self.er.show()
            else:
                item=self.listWidget_17.item(1)
                item.setText("Pourcentage De Décès: "+str((nb*100)//len(list_p))+"%")
        elif(self.radioButton_23.isChecked()):
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.setColumnCount(4)
            l1=list()
            for i in list_p:
                dict_pr={'cin':'','nom':'','prenom':'','prc':''}
                rq=0
                dict_pr['cin']=i['cin']
                dict_pr['nom']=i['nom']
                dict_pr['prenom']=i['prenom']
                if(int(i['age'])>70):
                    rq+=20
                elif(int(i['age'])>=50):
                   rq+=10
                for j in list_m:
                    if(j['cin']==i['cin']):
                        if(j['nom_m']=="DIABETE"):
                            rq+=15
                        elif(j['nom_m']=="HYPERTENSION"):
                            rq+=20
                        elif(j['nom_m']=="ASTHME"):
                            rq+=20
                dict_pr['prc']=str(rq)+"%"
                l1.append(dict_pr)
            self.tableWidget_3.setRowCount(len(l1))
            for row in range(self.tableWidget_3.rowCount()):
                col=0
                for i in l1[row].values():
                    item = QTableWidgetItem(str(i))
                    self.tableWidget_3.setItem(row, col, item)
                    col+=1
            self.stackedWidget_3.setCurrentWidget(self.page_19)
            if(len(l1)==0):
                self.er=Form4()
                self.er.label.setText("Dictionnaire personne est vide !")
                self.er.show()

    def RA_maladie(self):
        if (not self.radioButton_15.isChecked() and not self.radioButton_16.isChecked() and not self.radioButton_17.isChecked() and not self.radioButton_18.isChecked() and not self.radioButton_19.isChecked() and not self.radioButton_9.isChecked()):
            self.er=Form4()
            self.er.label.setText(" Choisir une option !")
            self.er.show()
        elif(self.radioButton_16.isChecked()):
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.setRowCount(len(list_m))
            self.tableWidget_2.setColumnCount(4)
            for row in range(self.tableWidget_2.rowCount()):
                col=0
                for i in list_m[row].values():
                    item = QTableWidgetItem(str(i))
                    self.tableWidget_2.setItem(row, col, item)
                    col+=1
            self.stackedWidget_3.setCurrentWidget(self.page_11)
            if(len(list_m)==0):
                self.er=Form4()
                self.er.label.setText("Dictionnaire Maladie Est Vide !")
                self.er.show()
        elif(self.radioButton_18.isChecked()):
            nom_m=self.comboBox_6.currentText()
            self.listWidget_9.clear()
            if(nom_m==""):
                self.er=Form4()
                self.er.label.setText("Aucun element à Afficher !")
                self.er.show()
            else:
                l=list()
                for i in list_m:
                    if(i['nom_m']==nom_m):
                        l.append(i)

            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.setRowCount(len(l))
            self.tableWidget_2.setColumnCount(4)
            for row in range(self.tableWidget_2.rowCount()):
                col=0
                for i in l[row].values():
                    item = QTableWidgetItem(str(i))
                    self.tableWidget_2.setItem(row, col, item)
                    col+=1
            self.stackedWidget_3.setCurrentWidget(self.page_11)
            if(len(l)==0):
                self.er=Form4()
                self.er.label.setText("Dictionnaire Maladie Est Vide !")
                self.er.show()
        elif(self.radioButton_17.isChecked()):
            cin=self.comboBox_7.currentText()
            self.tableWidget_2.setRowCount(0)
            if(cin==""):
                self.er=Form4()
                self.er.label.setText("Aucun element à Afficher !")
                self.er.show()
            else:
                l1=list()
                for i in list_m:
                    if(i['cin']==cin):
                        l1.append(i)
                self.tableWidget_2.setRowCount(len(l1))
                self.tableWidget_2.setColumnCount(4)
                for row in range(self.tableWidget_2.rowCount()):
                    col=0
                    for i in l1[row].values():
                        item = QTableWidgetItem(str(i))
                        self.tableWidget_2.setItem(row, col, item)
                        col+=1
                self.stackedWidget_3.setCurrentWidget(self.page_11)
                if(len(l1)==0):
                    self.er=Form4()
                    self.er.label.setText("Cet Personne n'ayant Aucune Maladie !")
                    self.er.show()
        elif(self.radioButton_15.isChecked()):
            l1=list()
            for i in list_m:
                dict_pr={'nom':'','pourcentage':''}
                nb=0
                nom_m=i['nom_m']
                dict_pr['nom']=nom_m
                for j in list_m:
                    if(j['nom_m']==nom_m):
                        nb+=1
                dict_pr['pourcentage']=str((nb*100)//len(list_m))+"%"
                test=0
                for i in l1:
                    if(i==dict_pr):
                        test=1
                if(test==0):
                    l1.append(dict_pr)
            self.tableWidget_5.setRowCount(len(l1))
            self.tableWidget_5.setColumnCount(2)
            for row in range(self.tableWidget_5.rowCount()):
                col=0
                for i in l1[row].values():
                    item = QTableWidgetItem(str(i))
                    self.tableWidget_5.setItem(row, col, item)
                    col+=1
                self.stackedWidget_3.setCurrentWidget(self.page_14)
                if(len(l1)==0):
                    self.er=Form4()
                    self.er.label.setText("Dictionnaire Maladie Est Vide !")
                    self.er.show()
        elif(self.radioButton_19.isChecked()):
            l1=list()
            for i in list_p:
                dict_pr={'cin': '','nom': '', 'prenom': '', 'nom_m':'','age': '', 'tel': '', 'dcd': ''}
                cin=i['cin']
                dict_pr['cin']=i['cin']
                dict_pr['nom']=i['nom']
                dict_pr['prenom']=i['prenom']
                dict_pr['age']=i['age']
                dict_pr['tel']=i['tel']
                dict_pr['dcd']=i['dcd']

                for j in list_m:
                    if(j['cin']==cin):
                        dict_pr['nom_m']=str(j['nom_m']+"\n"+dict_pr['nom_m'])
                l1.append(dict_pr)
            self.tableWidget_6.setRowCount(len(list_p))
            self.tableWidget_6.setColumnCount(7)
            for row in range(self.tableWidget_6.rowCount()):
                col=0
                for i in l1[row].values():
                    item = QTableWidgetItem(str(i))
                    self.tableWidget_6.setItem(row, col, item)
                    col+=1
            self.tableWidget_6.resizeRowsToContents()
            self.tableWidget_6.resizeColumnToContents(3)
            self.stackedWidget_3.setCurrentWidget(self.page_15)
            if(len(list_p)==0):
                self.er=Form4()
                self.er.label.setText("Dictionnaire Personne Est Vide !")
                self.er.show()

        self.radioButton_15.setCheckable(False)
        self.radioButton_16.setCheckable(False)
        self.radioButton_17.setCheckable(False)
        self.radioButton_18.setCheckable(False)
        self.radioButton_19.setCheckable(False)
        self.radioButton_9.setCheckable(False)
        self.radioButton_15.setCheckable(True)
        self.radioButton_16.setCheckable(True)
        self.radioButton_17.setCheckable(True)
        self.radioButton_18.setCheckable(True)
        self.radioButton_19.setCheckable(True)
        self.radioButton_9.setCheckable(True)
        self.comboBox_6.hide()
        self.comboBox_7.hide()

    def modifier_maladie(self):
        global list_m
        global list_p
        if (not self.widget_10.isVisible() and not self.widget_11.isVisible() ):
            self.er=Form4()
            self.er.label.setText(" Choisir une option de modification !")
            self.er.show()
        elif(self.widget_10.isVisible() ):
            cin=self.comboBox_3.currentText()
            nom=self.comboBox_4.currentText()
            nbr=self.lineEdit_24.text()
            if(cin=="" or nom==" "):
                self.er=Form4()
                self.er.label.setText("Aucun element à modifier !")
                self.er.show()
            elif(nbr=="" or int(nbr)<1):
                self.er=Form4()
                self.er.label.setText("Nouveau Nombre D'annee Invalid !")
                self.er.show()
            elif(not self.verif_nbr(cin,nbr,list_p)):
                self.er=Form4()
                self.er.label.setText("Nombre d'Annee Depasse l'age de personne !")
                self.er.show()
            else:
                for i in list_m:
                    if(cin==i['cin'] and nom==i['nom_m']):
                        i['nb']=nbr
                self.er=Form5()
                self.er.label.setText("Modification effectué !")
                self.er.show()
                self.widget_10.hide()
                self.radioButton_13.setCheckable(False)
                self.radioButton_13.setCheckable(True)
        elif(self.widget_11.isVisible()):
            cin=self.comboBox_5.currentText()
            if(cin==""):
                self.er=Form4()
                self.er.label.setText("Aucun element à modifier !")
                self.er.show()
            elif(self.radioButton_25.isChecked()==False and self.radioButton_26.isChecked()==False):
                self.er=Form4()
                self.er.label.setText("Choisir L'etat de décès !")
                self.er.show()
            else:
                if(self.radioButton_25.isChecked()):
                    dcd=1
                else:
                    dcd=0
                for i in list_p:
                    if(cin==i['cin']):
                        i['dcd']=dcd
                self.er=Form5()
                self.er.label.setText("Modification effectué !")
                self.er.show()
                self.widget_11.hide()
                self.radioButton_14.setCheckable(False)
                self.radioButton_14.setCheckable(True)

    def supprimer_maladie(self):
        maladie=self.comboBox_9.currentText()
        personne=self.comboBox_10.currentText()
        nbr=len(list_m)
        if(maladie==""):
            self.er=Form4()
            self.er.label.setText("Aucun element à supprimer !")
            self.er.show()
        elif(personne=="Tous Les Personnes"):
            i=0
            while(i<len(list_m)):
                if(list_m[i]['nom_m']==maladie):
                    list_m.pop(i)
                else:
                    i+=1
            self.comboBox_9.clear()
            self.comboBox_10.clear()
            for i in list_m:
                if(self.comboBox_9.findText(i['nom_m'])==-1):
                    self.comboBox_9.addItem(str(i['nom_m']))
            self.comboBox_10.addItem("Tous Les Personnes")
            for i in list_m:
                if(self.comboBox_10.findText(i['cin'])==-1):
                    self.comboBox_10.addItem(str(i['cin']))
            self.er=Form5()
            self.er.label.setText("Suppression effectué !")
            self.er.show()
        else:
            for i in list_m:
                if(maladie==i['nom_m'] and i['cin']==personne):
                    list_m.remove(i)
            if(nbr==len(list_m)):
                self.er=Form4()
                self.er.label.setText("Cet Personne n'ayant pas cette maladie !")
                self.er.show()
            else:
                self.comboBox_9.clear()
                self.comboBox_10.clear()
                for i in list_m:
                    if(self.comboBox_9.findText(i['nom_m'])==-1):
                        self.comboBox_9.addItem(str(i['nom_m']))
                self.change_personne()
                self.er=Form5()
                self.er.label.setText("Suppression effectué !")
                self.er.show()

    def ajout_m(self):
        global list_m
        self.er=Form4()
        cin=self.lineEdit_10.text()
        nom_m=self.lineEdit_9.text()
        l_code=list()
        for i in list_m:
            l_code.append(i['code'])

        code=max(l_code)+1
        nb=self.lineEdit_11.text()

        #controle
        if(not nom_m.isalpha()or len(nom_m)<3 or self.ch_correct(nom_m)==False):
            self.er.label.setText("Nom Invalid !")
            self.er.show()
        elif(not cin.isdigit() or len(cin)!=8):
            self.er.label.setText("Cin Invalid !")
            self.er.show()
        elif(self.unique_c(cin,list_p)==True):
            self.er.label.setText("Cin Inexistant  !")
            self.er.show()
        elif( nb=="" or int(nb)<=0 or not self.verif_nbr(cin,nb,list_p)):
            self.er.label.setText("Nombre d'Annee Invalid !")
            self.er.show()
        elif(not self.verif_nbr(cin,nb,list_p)):
            self.er.label.setText("Nombre d'Annee Depasse l'age de personne !")
            self.er.show()
        elif(not self.verif_cin(cin,nom_m,list_m)):
            self.er.label.setText("Les Données Existe Déjà !")
            self.er.show()
        else:
            dict_m['cin']=cin
            dict_m['nom_m']=nom_m.upper()
            dict_m['code']=code
            dict_m['nb']=nb
            list_m.append(dict_m)

            self.actualiser_m()
            self.er=Form5()
            self.er.label.setText("Ajout Effectué !")
            self.er.show()

    def verif_cin(self,ch1,ch2,l):
        for i in l:
            if(ch1==i['cin'] and i['nom_m']==ch2.upper()):
                return False
        return True

    def verif_nbr(self,ch,x,l):
        for i in l:
            if(ch==i['cin'] and i['age']<x):
                return False
        return True

    def RA_personne(self):
        global list_p

        if (not self.radioButton_10.isChecked() and not self.radioButton_6.isChecked() and not self.radioButton_7.isChecked() and not self.radioButton_5.isChecked() and not self.radioButton_8.isChecked() and not self.radioButton_9.isChecked()):
            self.er=Form4()
            self.er.label.setText(" Choisir une option !")
            self.er.show()
        elif(self.radioButton_10.isChecked()):
            self.tableWidget.setRowCount(0)
            self.tableWidget.setRowCount(len(list_p))
            self.tableWidget.setColumnCount(11)
            for row in range(self.tableWidget.rowCount()):
                col=0
                for i in list_p[row].values():
                    item = QTableWidgetItem(str(i))
                    self.tableWidget.setItem(row, col, item)
                    col+=1
            self.stackedWidget_3.setCurrentWidget(self.page_6)
            if(len(list_p)==0):
                self.er=Form4()
                self.er.label.setText("Dictionnaire Personne Est Vide !")
                self.er.show()
        elif(self.radioButton_6.isChecked()):
            self.tableWidget.setRowCount(0)
            tel=self.listWidget_6.currentText()
            self.tableWidget.setColumnCount(11)
            if(tel==""):
                self.er=Form4()
                self.er.label.setText("Aucun element à Afficher !")
                self.er.show()
            else:
                l1=list()
                for i in list_p:
                    ts=i['tel']
                    if(tel[:2]==ts[:2]):
                        l1.append(i)
                self.tableWidget.setRowCount(len(l1))
                self.tableWidget.setColumnCount(11)
                for row in range(self.tableWidget.rowCount()):
                    col=0
                    for i in l1[row].values():
                        item = QTableWidgetItem(str(i))
                        self.tableWidget.setItem(row, col, item)
                        col+=1
                self.stackedWidget_3.setCurrentWidget(self.page_6)
        elif(self.radioButton_7.isChecked()):
            self.tableWidget.setRowCount(0)
            nat=self.listWidget_5.currentText()
            self.tableWidget.setColumnCount(11)
            if(nat==""):
                self.er=Form4()
                self.er.label.setText("Aucun element à Afficher !")
                self.er.show()
            else:
                l1=list()
                for i in list_p:
                    if(i['nationalite']==nat):
                        l1.append(i)

                self.tableWidget.setRowCount(len(l1))
                self.tableWidget.setColumnCount(11)
                for row in range(self.tableWidget.rowCount()):
                    col=0
                    for i in l1[row].values():
                        item = QTableWidgetItem(str(i))
                        self.tableWidget.setItem(row, col, item)
                        col+=1
                self.stackedWidget_3.setCurrentWidget(self.page_6)
        elif(self.radioButton_5.isChecked()):
            self.tableWidget.setRowCount(0)
            tel=self.listWidget_8.currentText()
            self.tableWidget.setColumnCount(11)
            if(tel==""):
                self.er=Form4()
                self.er.label.setText("Aucun element à Afficher !")
                self.er.show()
            else:
                l1=list()
                for i in list_p:
                    if(i['tel']==tel):
                        l1.append(i)

                self.tableWidget.setRowCount(len(l1))
                self.tableWidget.setColumnCount(11)
                for row in range(self.tableWidget.rowCount()):
                    col=0
                    for i in l1[row].values():
                        item = QTableWidgetItem(str(i))
                        self.tableWidget.setItem(row, col, item)
                        col+=1
                self.stackedWidget_3.setCurrentWidget(self.page_6)
        elif(self.radioButton_8.isChecked()):
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(11)
            l1=list()
            for i in list_p:
                if(int(i['dcd'])==1):
                    l1.append(i)
            self.tableWidget.setRowCount(len(l1))
            self.tableWidget.setColumnCount(11)
            for row in range(self.tableWidget.rowCount()):
                col=0
                for i in l1[row].values():
                    item = QTableWidgetItem(str(i))
                    self.tableWidget.setItem(row, col, item)
                    col+=1
            self.stackedWidget_3.setCurrentWidget(self.page_6)
            if(len(l1)==0):
                self.er=Form4()
                self.er.label.setText("Aucun personne Décédé !")
                self.er.show()
        else:
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(11)
            l1=list()
            for i in list_p:
                if(int(i['dcd'])==0):
                    l1.append(i)
            self.tableWidget.setRowCount(len(l1))
            self.tableWidget.setColumnCount(11)
            for row in range(self.tableWidget.rowCount()):
                col=0
                for i in l1[row].values():
                    item = QTableWidgetItem(str(i))
                    self.tableWidget.setItem(row, col, item)
                    col+=1
            self.stackedWidget_3.setCurrentWidget(self.page_6)
            if(len(l1)==0):
                self.er=Form4()
                self.er.label.setText("Aucun personne Non-Décédé !")
                self.er.show()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.resizeColumnToContents(1)
        self.tableWidget.resizeColumnToContents(2)
        self.tableWidget.resizeColumnToContents(4)
        self.tableWidget.resizeColumnToContents(5)

    def modifier_personne(self):
        global list_p
        if (not self.widget_3.isVisible() and not self.widget_9.isVisible() ):
            self.er=Form4()
            self.er.label.setText(" Choisir une option de modification !")
            self.er.show()
        elif(self.widget_3.isVisible() ):
            cin=self.comboBox.currentText()
            ntel=self.lineEdit_22.text()
            if(cin==""):
                self.er=Form4()
                self.er.label.setText("Aucun element à modifier !")
                self.er.show()
            elif(not ntel.isdigit() or len(ntel)!=8):
                self.er=Form4()
                self.er.label.setText("Nouveau N° Telephone Invalid !")
                self.er.show()
            elif(self.unique_t(ntel,list_p)==False):
                self.er=Form4()
                self.er.label.setText("Telephone Déjà Existe !")
                self.er.show()
            else:
                for i in list_p:
                    if(cin==i['cin']):
                        i['tel']=ntel
                self.er=Form5()
                self.er.label.setText("Modification effectué !")
                self.er.show()
                self.lineEdit_22.clear()
                self.widget_3.hide()
                self.radioButton_11.setCheckable(False)
                self.radioButton_11.setCheckable(True)
        elif(self.widget_9.isVisible()):
            cin=self.comboBox_2.currentText()
            adresse=self.lineEdit_23.text()
            if(cin==""):
                self.er=Form4()
                self.er.label.setText("Aucun element à modifier !")
                self.er.show()
            elif(len(adresse)<5 or self.ch_correct(adresse)==False):
                self.er=Form4()
                self.er.label.setText("Adresse Invalid !")
                self.er.show()
            elif(not self.P_mot(adresse)):
                self.er=Form4()
                self.er.label.setText("Adresse Invalid !")
                self.er.show()
            else:
                for i in list_p:
                    if(cin==i['cin']):
                        i['adresse']=adresse.title()
                self.er=Form5()
                self.er.label.setText("Modification effectué !")
                self.er.show()
                self.widget_9.hide()
                self.lineEdit_23.clear()
                self.radioButton_12.setCheckable(False)
                self.radioButton_12.setCheckable(True)

    def supprimer_personne(self):
        global list_p
        if (not self.radioButton_2.isChecked() and not self.radioButton_3.isChecked() and not self.radioButton_4.isChecked()):
            self.er=Form4()
            self.er.label.setText(" Choisir option de suppression !")
            self.er.show()
        elif(self.radioButton_2.isChecked()):
            cin=self.listWidget_1.currentText()
            if(cin==""):
                self.er=Form4()
                self.er.label.setText("Aucun element à supprimer !")
                self.er.show()
            else:
                for i in list_p:
                    if(cin==i['cin']):
                        list_p.remove(i)
                i=0
                while(i<len(list_m)):
                    if(list_m[i]['cin']==cin):
                        list_m.pop(i)
                    else:
                        i+=1
                self.er=Form5()
                self.er.label.setText("Suppression effectué !")
                self.er.show()
        elif(self.radioButton_3.isChecked()):
            nationalite=self.listWidget_2.currentText()
            if(nationalite==""):
                self.er=Form4()
                self.er.label.setText("Aucun element à supprimer !")
                self.er.show()
            else:
                i=0
                while( i <len(list_p)):
                    ns=list_p[i]['nationalite']
                    if(nationalite==ns):
                        j=0
                        while(j<len(list_m)):
                            if(list_m[j]['cin']==list_p[i]['cin']):
                                list_m.pop(j)
                            else:
                                j+=1
                        list_p.pop(i)
                    else:
                        i+=1
                self.er=Form5()
                self.er.label.setText("Suppression effectué !")
                self.er.show()
        elif(self.radioButton_4.isChecked()):
            tel=self.listWidget_3.currentText()
            if(tel==""):
                self.er=Form4()
                self.er.label.setText("Aucun element à supprimer !")
                self.er.show()
            else:
                i=0
                while( i <len(list_p)):
                    ts=list_p[i]['tel']
                    if(tel[:2]==ts[:2]):
                        j=0
                        while(j<len(list_m)):
                            if(list_m[j]['cin']==list_p[i]['cin']):
                                list_m.pop(j)
                            else:
                                j+=1
                        list_p.pop(i)
                    else:
                        i+=1
                self.er=Form5()
                self.er.label.setText("Suppression effectué !")
                self.er.show()
        self.listWidget_1.clear()
        self.listWidget_2.clear()
        self.listWidget_3.clear()
        self.listWidget_1.hide()
        self.listWidget_2.hide()
        self.listWidget_3.hide()

        self.radioButton_2.setCheckable(False)
        self.radioButton_2.setCheckable(True)

        self.radioButton_3.setCheckable(False)
        self.radioButton_3.setCheckable(True)

        self.radioButton_4.setCheckable(False)
        self.radioButton_4.setCheckable(True)
        for i in list_p:
            self.listWidget_1.addItem(i['cin'])
            if(self.listWidget_2.findText(i['nationalite'])==-1):
                self.listWidget_2.addItem(i['nationalite'])
            if(self.listWidget_3.findText(i['tel'][:2]+" *** ***")==-1):
                self.listWidget_3.addItem(i['tel'][:2]+" *** ***")

    def enregister_personne(self):
        with open(r"Personne.dat", "wb") as f:
            json_list = json.dumps(list_p)
            encoded_list = base64.b64encode(json_list.encode('utf-8'))
            pk.dump(encoded_list, f)
        self.er=Form6()
        self.er.label2.setText("Dictionnaire Personne Enregistré !")
        self.er.show()

    def enregister_maladie(self):
        with open(r"Maladie.dat", "wb") as f:
            json_list = json.dumps(list_m)
            encoded_list = base64.b64encode(json_list.encode('utf-8'))
            pk.dump(encoded_list, f)
        self.er=Form6()
        self.er.label2.setText("Dictionnaire Maladie Enregistré !")
        self.er.show()

    def enregister_tt(self):
        with open(r"Personne.dat", "wb") as f:
            json_list = json.dumps(list_p)
            encoded_list = base64.b64encode(json_list.encode('utf-8'))
            pk.dump(encoded_list, f)
        with open(r"Maladie.dat", "wb") as f:
            json_list = json.dumps(list_m)
            encoded_list = base64.b64encode(json_list.encode('utf-8'))
            pk.dump(encoded_list, f)
        self.er=Form6()
        self.er.label2.setText("Enregistrement Effectuée !")
        self.er.show()

    def ajout_p(self):
        global list_p
        self.er=Form4()
        cin=self.lineEdit.text()
        nom=self.lineEdit_2.text()
        prenom=self.lineEdit_3.text()
        age=self.lineEdit_4.text()
        adresse=self.lineEdit_5.text()
        nationalite=self.lineEdit_6.text()
        tel=self.lineEdit_7.text()
        selected_date = self.dateEdit.date()
        year = selected_date.year()
        month = selected_date.month()
        day = selected_date.day()
        d1 = QDate.currentDate().day()
        m1 = QDate.currentDate().month()
        y1 = QDate.currentDate().year()
        if self.radioButton.isChecked():
            dcd=1
        elif self.radioButton_24.isChecked():
            dcd=0

        #controle
        if(not cin.isdigit() or len(cin)!=8):
            self.er.label.setText("Cin Invalid !")
            self.er.show()
        elif(self.unique_c(cin,list_p)==False):
            self.er.label.setText("Cin Déjà Existe !")
            self.er.show()
        elif(len(nom)<3 or self.ch_correct(nom)==False):
            self.er.label.setText("Nom Invalid !")
            self.er.show()
        elif(not self.P_mot(nom)):
            self.er.label.setText("Nom Invalid !")
            self.er.show()
        elif(not prenom.isalpha()or len(prenom)<3 or self.ch_correct(prenom)==False):
            self.er.label.setText("Prenom Invalid !")
            self.er.show()
        elif( age=="" or int(age)<=0):
            self.er.label.setText("Age Invalid !")
            self.er.show()
        elif(len(adresse)<5 or self.ch_correct(adresse)==False):
            self.er.label.setText("Adresse Invalid !")
            self.er.show()
        elif(not self.P_mot(adresse)):
            self.er.label.setText("Adresse Invalid !")
            self.er.show()
        elif(not nationalite.isalpha()or len(nationalite)<5 or self.ch_correct(nationalite)==False):
            self.er.label.setText("Nationalite Invalide !")
            self.er.show()
        elif(not tel.isdigit() or len(tel)!=8):
            self.er.label.setText("Telephone Invalid !")
            self.er.show()
        elif(self.unique_t(tel,list_p)==False):
            self.er.label.setText("Telephone Déjà Existe !")
            self.er.show()
        elif(year>y1 or(year==y1 and month>m1) or (year==y1 and month==m1 and day>d1)):
            self.er.label.setText("Date D'Infection Invalid !")
            self.er.show()
        elif(self.radioButton_24.isChecked()==False and self.radioButton.isChecked()==False):
            self.er.label.setText("Etat Décès Invalid !")
            self.er.show()
        else:
            dict_p['cin']=cin
            dict_p['nom']=nom.upper()
            dict_p['prenom']=prenom.capitalize()
            dict_p['age']=age
            dict_p['adresse']=adresse.title()
            dict_p['nationalite']=nationalite.upper()
            dict_p['tel']=tel
            dict_p['jr']=day
            dict_p['ms']=month
            dict_p['an']=year
            dict_p['dcd']=dcd
            list_p.append(dict_p)

            self.actualiser_p()
            self.er=Form5()
            self.er.label.setText("Ajout Effectué !")
            self.er.show()
    def P_mot(self,ch):
        if(ch[0].isspace() or ch[-1].isspace()):
            return False
        for i in range(len(ch)-1):
            if(ch[i].isspace() and ch[i+1].isspace()):
                return False
        for i in range(len(ch)):
            if(not(ch[i].isalpha() or ch[i].isspace())):
                return False
        return True

    def ch_correct(self,ch):
        for i in range(1,len(ch)-1):
            if(ch[i-1]==ch[i] and ch[i]==ch[i+1]):
                return False
        return True
    def actualiser_m(self):
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
    def actualiser_p(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.dateEdit.setDate(QDate(2020,1,1))
        self.radioButton.setCheckable(False)
        self.radioButton.setCheckable(True)
        self.radioButton_24.setCheckable(False)
        self.radioButton_24.setCheckable(True)


    def unique_c(self,ch,l):
        for i in l:
            if(ch==i['cin']):
                return False
        return True
    def unique_t(self,ch,l):
        for i in l:
            if(ch==i['tel']):
                return False
        return True
    def unique_cd(self,ch,l):
        for i in l:
            if(ch==i['code']):
                return False
        return True

    def rch_aff(self):
        if self.radioButton_10.isChecked():
            self.listWidget_6.hide()
            self.listWidget_5.hide()
            self.listWidget_8.hide()
        elif self.radioButton_9.isChecked():
            self.listWidget_6.hide()
            self.listWidget_5.hide()
            self.listWidget_8.hide()
        elif self.radioButton_8.isChecked():
            self.listWidget_6.hide()
            self.listWidget_5.hide()
            self.listWidget_8.hide()
        elif self.radioButton_6.isChecked():
            self.listWidget_6.show()
            self.listWidget_5.hide()
            self.listWidget_8.hide()
        elif self.radioButton_7.isChecked():
            self.listWidget_5.show()
            self.listWidget_6.hide()
            self.listWidget_8.hide()
        else:
            self.listWidget_8.show()
            self.listWidget_5.hide()
            self.listWidget_6.hide()
    def sp_show(self):
        if self.radioButton_2.isChecked():
            self.listWidget_1.show()
            self.listWidget_2.hide()
            self.listWidget_3.hide()
        elif self.radioButton_3.isChecked():
            self.listWidget_2.show()
            self.listWidget_1.hide()
            self.listWidget_3.hide()
        else:
            self.listWidget_3.show()
            self.listWidget_2.hide()
            self.listWidget_1.hide()

    def recup_done(self):
        global rcp
        rcp=True
        self.recup_pers()
        self.recup_mld()
        self.er=Form2()
        self.er.show()
    def E_recup(self):
        self.er=Form1()
        self.er.show()
    #Function link
    def B1(self):
        self.label_2.setText("ACCUIEL ")
        self.stackedWidget_3.setCurrentWidget(self.page_4)
        self.ACCUEIL.setCheckable(False)
        self.ACCUEIL.setCheckable(True)
    def B2(self):
        self.stackedWidget_3.setCurrentWidget(self.page)
        self.pushButton_5.setCheckable(False)
        self.label_2.setText("Mise A Jour Des Personnes  ")
        self.pushButton_5.setCheckable(True)
    def B3(self):
        self.listWidget_1.clear()
        self.listWidget_2.clear()
        self.listWidget_3.clear()
        self.stackedWidget_3.setCurrentWidget(self.page_2)
        self.label_2.setText("Mise A Jour Des Personnes  ")
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setCheckable(True)
        for i in list_p:
            self.listWidget_1.addItem(i['cin'])
            if(self.listWidget_2.findText(i['nationalite'])==-1):
                self.listWidget_2.addItem(i['nationalite'])
            if(self.listWidget_3.findText(i['tel'][:2]+" *** ***")==-1):
                self.listWidget_3.addItem(i['tel'][:2]+" *** ***")
    def B4(self):
        self.comboBox.clear()
        self.comboBox_2.clear()
        self.stackedWidget_3.setCurrentWidget(self.page_3)
        self.label_2.setText("Mise A Jour Des Personnes  ")
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setCheckable(True)
        for i in list_p:
            self.comboBox.addItem(i['cin'])
            self.comboBox_2.addItem(i['cin'])
    def B5(self):
        self.listWidget_6.clear()
        self.listWidget_5.clear()
        self.listWidget_8.clear()
        self.stackedWidget_3.setCurrentWidget(self.page_5)
        self.label_2.setText("Recherche Et Affichage Des Personnes")
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setCheckable(True)
        for i in list_p:
            if(self.listWidget_5.findText(i['nationalite'])==-1):
                self.listWidget_5.addItem(i['nationalite'])
            self.listWidget_8.addItem(i['tel'])
            if(self.listWidget_6.findText(i['tel'][:2]+" *** ***")==-1):
                self.listWidget_6.addItem(i['tel'][:2]+" *** ***")
    def B6(self):
        self.stackedWidget_3.setCurrentWidget(self.page_7)
        self.label_2.setText("Mise A Jour Des Maladies  ")
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setCheckable(True)
    def B7(self):
        self.comboBox_9.clear()
        self.stackedWidget_3.setCurrentWidget(self.page_8)
        self.label_2.setText("Mise A Jour Des Maladies  ")
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setCheckable(True)
        for i in list_m:
            if(self.comboBox_9.findText(i['nom_m'])==-1):
                self.comboBox_9.addItem(str(i['nom_m']))
        self.change_personne()

    def B8(self):
        self.comboBox_3.clear()
        self.comboBox_4.clear()

        for i in list_m:
            if(self.comboBox_3.findText(i['cin'])==-1):
               self.comboBox_3.addItem(str(i['cin']))
            if(self.comboBox_5.findText(i['cin'])==-1):
               self.comboBox_5.addItem(str(i['cin']))
        self.change_item()
        self.stackedWidget_3.setCurrentWidget(self.page_9)
        self.label_2.setText("Mise A Jour Des Maladies  ")
        self.pushButton_10.setCheckable(False)
        self.pushButton_10.setCheckable(True)
    def B9(self):
        self.comboBox_6.clear()
        self.comboBox_7.clear()
        for i in list_p:
            self.comboBox_7.addItem(i['cin'])
        for i in list_m:
            if(self.comboBox_6.findText(i['nom_m'])==-1):
                self.comboBox_6.addItem(i['nom_m'])
        self.stackedWidget_3.setCurrentWidget(self.page_10)
        self.label_2.setText("Recherche Et  Affichage Des Maladies ")
        self.pushButton_11.setCheckable(False)
        self.pushButton_11.setCheckable(True)
    def B10(self):
        self.comboBox_8.clear()
        for i in list_p:
            if(self.comboBox_8.findText(i['nationalite'])==-1):
                self.comboBox_8.addItem(i['nationalite'])
        if(rcp==True):
            self.stackedWidget_3.setCurrentWidget(self.page_16)
            self.label_2.setText("Statistique ")
            self.calcul_affi.setCheckable(False)
            self.calcul_affi.setCheckable(True)
        else:
            self.E_recup()
    #Enregistrement menu
    def Enr(self):
        if(self.enreg.isChecked() and rcp == True):
            self.widget_8.show()
            self.enreg.setCheckable(False)
        elif(self.enreg.isChecked() and rcp == False):
            self.E_recup()
        else:
            self.widget_8.hide()
            self.enreg.setCheckable(True)

    #Maladie menu

    def M_mal(self):
        if(self.pushButton_7.isChecked()):
            self.widget_7.show()
            self.pushButton_7.setIcon(QIcon("Source/Fld.png"))
            self.pushButton_7.setCheckable(False)
        else:
            self.widget_7.hide()
            self.pushButton_7.setIcon(QIcon("Source/Fl.png"))
            self.pushButton_7.setCheckable(True)
    def mal(self):
        if(self.G_maladie.isChecked() and rcp == True):
            self.widget_6.show()
            self.G_maladie.setCheckable(False)
        elif(self.G_maladie.isChecked() and rcp == False):
            self.E_recup()
        else:
            self.widget_6.hide()
            self.G_maladie.setCheckable(True)
    #Peronne menu

    def M_pers(self):
        if(self.pushButton_2.isChecked()):
            self.widget_5.show()
            self.pushButton_2.setIcon(QIcon("Source/Fld.png"))
            self.pushButton_2.setCheckable(False)
        else:
            self.widget_5.hide()
            self.pushButton_2.setCheckable(True)
            self.pushButton_2.setIcon(QIcon("Source/Fl.png"))
    def pers(self):
        if(self.G_personnes.isChecked() and rcp == True):
            self.widget_4.show()
            self.G_personnes.setCheckable(False)
        elif(self.G_personnes.isChecked() and rcp == False):
            self.E_recup()
        else:
            self.widget_4.hide()
            self.G_personnes.setCheckable(True)

    #Affichage Menu
    def menu(self):
        if(self.pushButton.isChecked()):
            self.widget_2.show()
            self.pushButton.setCheckable(False)
        else:
            self.widget_2.hide()
            self.pushButton.setCheckable(True)


    #center Window
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



stylesheet = """
    Ui {
        background-image: url("Source/2Fichier 1.png");
        background-repeat: no-repeat;
        background-position: center;
    }
"""

#App execute
app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(stylesheet)
window = Ui()
intro = MainWindow()
window.showFullScreen()
#intro.showFullScreen()
app.exec()
