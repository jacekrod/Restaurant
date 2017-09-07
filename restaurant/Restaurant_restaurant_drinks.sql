-- MySQL dump 10.13  Distrib 5.7.19, for Linux (x86_64)
--
-- Host: localhost    Database: Restaurant
-- ------------------------------------------------------
-- Server version	5.7.19-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `restaurant_drinks`
--

DROP TABLE IF EXISTS `restaurant_drinks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `restaurant_drinks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` decimal(5,1) NOT NULL,
  `drink_name` varchar(99),
  `drink_type` int(11),
  `drink_volume` int(11),
  `wine_colors` int(11),
  `wine_sweetness` int(11),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurant_drinks`
--

LOCK TABLES `restaurant_drinks` WRITE;
/*!40000 ALTER TABLE `restaurant_drinks` DISABLE KEYS */;
INSERT INTO `restaurant_drinks` VALUES (1,9.0,'jabłkowy',5,NULL,NULL,NULL),(2,8.5,'porzeczkowy',5,NULL,NULL,NULL),(3,8.0,'anansowy',5,NULL,NULL,NULL),(4,16.0,'Mohito',2,NULL,NULL,NULL),(5,19.0,'Sex On The Beach',2,NULL,NULL,NULL),(6,23.0,'Long Island Iced Tea',2,NULL,NULL,NULL),(7,12.0,'Bordoux',3,NULL,NULL,NULL),(8,9.0,'Coty',3,NULL,NULL,NULL),(9,6.0,'Okocim',4,NULL,NULL,NULL),(10,7.0,'Książęce',4,NULL,NULL,NULL),(11,15.0,'Somelier',3,NULL,NULL,NULL),(12,15.0,'Somelier',3,1,NULL,NULL),(13,35.0,'Bordooo',3,3,1,3),(14,35.0,'Bordooo',3,3,1,1);
/*!40000 ALTER TABLE `restaurant_drinks` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-09-07 16:00:48
