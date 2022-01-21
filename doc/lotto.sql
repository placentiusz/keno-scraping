CREATE DATABASE `lotto` /*!40100 DEFAULT CHARACTER SET latin1 */;
CREATE TABLE `results` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Number` int(11) NOT NULL,
  `Date` datetime NOT NULL,
  `Game` varchar(100) NOT NULL,
  `Result` text NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `Date` (`Date`),
  KEY `Id` (`Id`,`Number`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
