CREATE TABLE `socios` (
  `idsocio` int(11) NOT NULL AUTO_INCREMENT,
  `dni` varchar(45) DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idsocio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
