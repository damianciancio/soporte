CREATE TABLE `personas`.`persona` (
 `idpersona` INT NOT NULL AUTO_INCREMENT,
 `nombre` VARCHAR(30) NOT NULL,
 `fechaNacimiento` DATE NULL,
 `dni` INT(13) NULL,
 `altura` DECIMAL NULL,
 PRIMARY KEY (`idpersona`));


CREATE TABLE `personas`.`personapeso` (
 `idpersona` INT NOT NULL,
 `fecha` DATE NULL,
 `peso` DECIMAL NULL,
 PRIMARY KEY (`idpersona`),
 CONSTRAINT `fk_idpersona`
   FOREIGN KEY (`idpersona`)
   REFERENCES `personas`.`persona` (`idpersona`)
   ON DELETE CASCADE
   ON UPDATE CASCADE);