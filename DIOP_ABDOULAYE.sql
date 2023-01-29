DROP TABLE Competition
DROP TABLE Equipe
DROP TABLE Match
 
CREATE TABLE Competition 
      (nomCompetition VARCHAR2(18),
       typeCompetition VARCHAR2(16),
       annee NUMBER(4),
       paysOrganisateur VARCHAR2(18),
       CONSTRAINT nomCompet_pk PRIMARY KEY (nomCompetition));
       
       
CREATE TABLE Equipe
      (codeEquipe VARCHAR2(18),
       nomPays VARCHAR2(18),
       genre VARCHAR2(1),
       rangInternational NUMBER(4),
       CONSTRAINT codeEquipe_pk PRIMARY KEY (codeEquipe));
       
       
 CREATE TABLE Match
      (codeMatch VARCHAR2(10),
       date_M DATE,
       nomCompetition VARCHAR2(18),
       equipe1 VARCHAR2(18),
       equipe2 VARCHAR2(18),
       scoreEquipe1 NUMBER(2),
       scoreEquipe2 NUMBER(2),
       niveauCompetition VARCHAR2(16),
       CONSTRAINT equipe1_fk1 FOREIGN KEY (equipe1) REFERENCES Equipe(codeEquipe),
       CONSTRAINT nomCompetition_fk2 FOREIGN KEY (nomCompetition) REFERENCES Competition(nomCompetition),
       CONSTRAINT equipe2_fk3 FOREIGN KEY (equipe2) REFERENCES Equipe(codeEquipe),
       CONSTRAINT codeMatch_pk PRIMARY KEY (codeMatch));


alter table Match add constraint score check ( ( scoreEquipe1>=0) or (( scoreEquipe2>=0)) );
     


 1.SELECT nomCompetition,annee FROM Competition ;
 
 2.SELECT nomPays,rangInternational FROM Equipe  WHERE genre='h';
 
  3.SELECT codeEquipe FROM Equipe MINUS SELECT codeEquipe FROM Equipe  WHERE genre='h'; 
  
  4.SELECT codeMatch,date_M  FROM Match  WHERE nomCompetition='FIFA_2022' ; 

  5.SELECT equipe1 FROM Match WHERE (scoreEquipe1>scoreEquipe2)  UNION SELECT equipe2 FROM Match WHERE (scoreEquipe1<scoreEquipe2);

  6.SELECT nomCompetition,  rangInternational FROM Competition INTERSECT SELECT equipe1 FROM Match WHERE (scoreEquipe1>scoreEquipe2)  UNION SELECT equipe2 FROM Match WHERE (scoreEquipe1<scoreEquipe2);
  
  8.SELECT nomCompetition,  rangInternational FROM Competition MINUS SELECT equipe1 FROM Match WHERE (scoreEquipe1<scoreEquipe2)  UNION SELECT equipe2 FROM Match WHERE (scoreEquipe1>scoreEquipe2)
 

