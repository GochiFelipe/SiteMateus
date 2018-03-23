CREATE SCHEMA SITE_SHAKA;
/*

1 - ESPORTES
2 - CASAMENTO
3 - FORMATURA
4 - ANIVERSARIO

*/

CREATE TABLE IF NOT EXISTS `SITE_SHAKA`.`EVENTOS` (
  `ID_EVENTO` INT(11) NOT NULL AUTO_INCREMENT,
  `TIPO_EVENTO` INT(11) NOT NULL,
  `NOME_EVENTO` VARCHAR(125) NOT NULL,
  `LOCAL_EVENTO` VARCHAR(255) NOT NULL,
  `DATA_EVENTO` DATE NOT NULL,
  `URL_FOTO_EVENTO` VARCHAR(45) NOT NULL,
  `OBSERVACOES` VARCHAR(500) NULL,
  `ID_ARTE` INT(11) NULL,
  `ID_VIDEO` INT(11) NULL,
  `ID_ANTES_DEPOIS` INT(11) NULL,
  `ID_DIAGRAMA` INT(11) NULL,
  PRIMARY KEY (`ID_EVENTO`, `TIPO_EVENTO`, `NOME_EVENTO`, `LOCAL_EVENTO`, `DATA_EVENTO`, `URL_FOTO_EVENTO`),
  UNIQUE INDEX `idEVENTOS_UNIQUE` (`ID_EVENTO` ASC),
  UNIQUE INDEX `ID_ARTE_UNIQUE` (`ID_ARTE` ASC),
  UNIQUE INDEX `ID_VIDEO_UNIQUE` (`ID_VIDEO` ASC),
  UNIQUE INDEX `ID_ANTES_DEPOIS_UNIQUE` (`ID_ANTES_DEPOIS` ASC),
  UNIQUE INDEX `ID_DIAGRAMA_UNIQUE` (`ID_DIAGRAMA` ASC),
  UNIQUE INDEX `URL_EVENTOS_UNIQUE` (`URL_FOTO_EVENTO` ASC),
  UNIQUE INDEX `NOME_EVENTO_UNIQUE` (`NOME_EVENTO` ASC))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `SITE_SHAKA`.`CASAMENTOS` (
  `ID_CASAMENTO` INT(11) NOT NULL,
  `NOME_NOIVO` VARCHAR(45) NOT NULL,
  `NOME_NOIVA` VARCHAR(45) NOT NULL,
  `ID_FESTAS_CASAMENTO` INT(11) NULL,
  PRIMARY KEY (`ID_CASAMENTO`, `NOME_NOIVO`, `NOME_NOIVA`),
  INDEX `FK_CASAMENTO_EVENTO_idx` (`ID_CASAMENTO` ASC),
  UNIQUE INDEX `ID_CASAMENTO_UNIQUE` (`ID_CASAMENTO` ASC),
  INDEX `fk_CASAMENTOS_FESTAS1_idx` (`ID_FESTAS_CASAMENTO` ASC),
  CONSTRAINT `FK_CASAMENTO_EVENTO`
    FOREIGN KEY (`ID_CASAMENTO`)
    REFERENCES `SITE_SHAKA`.`EVENTOS` (`ID_EVENTO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_CASAMENTOS_FESTAS1`
    FOREIGN KEY (`ID_FESTAS_CASAMENTO`)
    REFERENCES `SITE_SHAKA`.`FESTAS` (`ID_FESTAS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `SITE_SHAKA`.`FESTAS` (
  `ID_FESTAS` INT(11) NOT NULL,
  PRIMARY KEY (`ID_FESTAS`),
  UNIQUE INDEX `ID_FESTAS_UNIQUE` (`ID_FESTAS` ASC),
  INDEX `FK_FESTA_EVENTO_idx` (`ID_FESTAS` ASC),
  CONSTRAINT `FK_FESTA_EVENTO`
    FOREIGN KEY (`ID_FESTAS`)
    REFERENCES `SITE_SHAKA`.`EVENTOS` (`ID_EVENTO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `SITE_SHAKA`.`ESPORTES` (
  `ID_ESPORTES` INT(11) NOT NULL,
  `NOME_ESPORTE` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID_ESPORTES`, `NOME_ESPORTE`),
  INDEX `FK_EVENTO_ESPORTE_idx` (`ID_ESPORTES` ASC),
  UNIQUE INDEX `ID_ESPORTES_UNIQUE` (`ID_ESPORTES` ASC),
  CONSTRAINT `FK_EVENTO_ESPORTE`
    FOREIGN KEY (`ID_ESPORTES`)
    REFERENCES `SITE_SHAKA`.`EVENTOS` (`ID_EVENTO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `SITE_SHAKA`.`ALBUNS` (
  `ID_ALBUM` INT(11) NOT NULL,
  `NOME_ALBUM` VARCHAR(125) NOT NULL,
  `URL_ALBUM` VARCHAR(255) NOT NULL,
  `TIPO_ALBUM` INT(11) NOT NULL,
  `DATA_ALBUM` DATE NOT NULL,
  PRIMARY KEY (`ID_ALBUM`, `NOME_ALBUM`, `URL_ALBUM`, `TIPO_ALBUM`, `DATA_ALBUM`),
  INDEX `FK_ALBUNS_EVENTOS_idx` (`DATA_ALBUM` ASC, `TIPO_ALBUM` ASC),
  UNIQUE INDEX `ID_ALBUN_UNIQUE` (`ID_ALBUM` ASC),
  CONSTRAINT `FK_ALBUNS_EVENTOS`
    FOREIGN KEY (`DATA_ALBUM` , `TIPO_ALBUM`)
    REFERENCES `SITE_SHAKA`.`EVENTOS` (`DATA_EVENTO` , `TIPO_EVENTO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `SITE_SHAKA`.`FESTAS_CASAMETOS` (
  `ID_FESTAS_CASAMETOS` INT(11) NOT NULL,
  `TEMA_CASAMENTO` VARCHAR(255) NULL,
  PRIMARY KEY (`ID_FESTAS_CASAMETOS`),
  CONSTRAINT `FK_FESTA`
    FOREIGN KEY (`ID_FESTAS_CASAMETOS`)
    REFERENCES `SITE_SHAKA`.`FESTAS` (`ID_FESTAS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `SITE_SHAKA`.`ANIVERSARIOS` (
  `ID_ANIVERSARIO` INT(11) NOT NULL,
  `NOME_ANIVERSARIANTE` VARCHAR(45) NOT NULL,
  `TEMA_ANIVERSARIO` VARCHAR(255) NULL,
  PRIMARY KEY (`ID_ANIVERSARIO`, `NOME_ANIVERSARIANTE`),
  UNIQUE INDEX `ID_ANIVERSARIO_UNIQUE` (`ID_ANIVERSARIO` ASC),
  CONSTRAINT `FK_FESTAS_ANIVERSARIOS`
    FOREIGN KEY (`ID_ANIVERSARIO`)
    REFERENCES `SITE_SHAKA`.`FESTAS` (`ID_FESTAS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `SITE_SHAKA`.`FORMATURAS` (
  `ID_FORMATURA` INT(11) NOT NULL,
  `NOME_TURMA` VARCHAR(255) NULL,
  `NOME_FORMANDO` VARCHAR(45) NULL,
  `CURSO_FORMATURA` VARCHAR(45) NULL,
  PRIMARY KEY (`ID_FORMATURA`),
  UNIQUE INDEX `ID_FORMATURA_UNIQUE` (`ID_FORMATURA` ASC),
  CONSTRAINT `FK_FESTA_FORMATURA`
    FOREIGN KEY (`ID_FORMATURA`)
    REFERENCES `SITE_SHAKA`.`FESTAS` (`ID_FESTAS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

##################################################################################################################

insert into SITE_SHAKA.EVENTOS (TIPO_EVENTO, NOME_EVENTO, LOCAL_EVENTO, DATA_EVENTO, URL_FOTO_EVENTO)
			VALUES (1, 'OiJam', 'Saquarema', '2018-03-20', 'teste');
insert into SITE_SHAKA.ESPORTES ( ID_ESPORTES, NOME_ESPORTE)
			VALUES ((SELECT LAST_INSERT_ID(ID_EVENTO) FROM EVENTOS WHERE TIPO_EVENTO = 1), 'Surf');
            
##################################################################################################################
            
insert into SITE_SHAKA.EVENTOS(TIPO_EVENTO, NOME_EVENTO, LOCAL_EVENTO, DATA_EVENTO, URL_FOTO_EVENTO)
			VALUES (2, 'Casamento Arnaldo e Luana', 'Praia da Bica', '2018-05-20', 'teste casamento');
insert into SITE_SHAKA.CASAMENTOS(ID_CASAMENTO, NOME_NOIVO, NOME_NOIVA)
			VALUES((SELECT MAX(ID_EVENTO) FROM EVENTOS WHERE TIPO_EVENTO = 2), 'Arnaldo', 'Luana');

##################################################################################################################

INSERT INTO SITE_SHAKA.EVENTOS(TIPO_EVENTO, NOME_EVENTO, LOCAL_EVENTO, DATA_EVENTO, URL_FOTO_EVENTO)
			VALUES (2, 'Casamento Felipe e Kamylla', 'Ilha do Japones', '2021-04-04', 'teste casamento com festa');
INSERT INTO SITE_SHAKA.CASAMENTOS(ID_CASAMENTO, NOME_NOIVO, NOME_NOIVA, ID_FESTAS_CASAMENTO)
			VALUES((SELECT MAX(ID_EVENTO) FROM EVENTOS WHERE TIPO_EVENTO = 2), 'Felipe', 'Kamylla',
            (SELECT ID_EVENTO FROM EVENTOS WHERE TIPO_EVENTO = 2));
INSERT INTO SITE_SHAKA.FESTAS(ID_FESTAS) 
			VALUES((SELECT MAX(ID_EVENTO)
							FROM CASAMENTOS c
                            LEFT JOIN EVENTOS e
                            ON e.TIPO_EVENTO = 2
                            AND e.ID_EVENTO = c.ID_CASAMENTO));
INSERT INTO SITE_SHAKA.FESTAS_CASAMENTOS(ID_FESTAS_CASAMETOS, TEMA_CASAMENTO)
			VALUES((SELECT MAX(ID_FESTA)
            FROM FESTAS f 
            LEFT JOIN EVENTOS e 
            ON e.TIPO_EVENTO = 2 
            AND e.ID_EVENTO = c.ID_CASAMENTO), 'Lual');

##################################################################################################################

INSERT INTO SITE_SHAKA.EVENTOS(TIPO_EVENTO, NOME_EVENTO, LOCAL_EVENTO, DATA_EVENTO, URL_FOTO_EVENTO)
			VALUES (3, 'Formatura Colegio Naval', 'Colegio Naval', '2021-04-04', 'teste formatura');
INSERT INTO SITE_SHAKA.FESTAS(ID_FESTAS)
			VALUES((SELECT MAX(ID_EVENTO) FROM EVENTOS WHERE TIPO_EVENTO = 3));
INSERT INTO SITE_SHAKA.FORMATURAS(ID_FORMATURA, NOME_TURMA, NOME_FORMANDO, CURSO_FORMATURA)
			VALUES((SELECT MAX(ID_FESTAS) 
            FROM FESTAS), 'Turma de 2016', 'Vinicius Neves', 'Colégio Naval');
            
##################################################################################################################

INSERT INTO SITE_SHAKA.EVENTOS(TIPO_EVENTO, NOME_EVENTO, LOCAL_EVENTO, DATA_EVENTO, URL_FOTO_EVENTO)
			VALUES (4, 'Aniversário da Carla', "Carla's Birthday", '2019-02-18', 'teste aniversário');
INSERT INTO SITE_SHAKA.FESTAS(ID_FESTAS)
			VALUES((SELECT MAX(ID_EVENTO) FROM EVENTOS WHERE TIPO_EVENTO = 4));
INSERT INTO SITE_SHAKA.ANIVERSARIOS(ID_ANIVERSARIO, NOME_ANIVERSARIANTE, TEMA_ANIVERSARIO)
			VALUES((SELECT MAX(ID_FESTAS) 
            FROM FESTAS),'Carla', 'Princessa Fiona');
