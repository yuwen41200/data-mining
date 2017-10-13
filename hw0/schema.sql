-- MySQL dump 10.16  Distrib 10.2.9-MariaDB, for osx10.12 (x86_64)
--
-- Host: localhost    Database: dm
-- ------------------------------------------------------
-- Server version	10.2.9-MariaDB

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
-- Table structure for table `Power`
--

DROP TABLE IF EXISTS `Power`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Power` (
  `updateTime` datetime NOT NULL,
  `northSupply` double DEFAULT NULL,
  `northUsage` double DEFAULT NULL,
  `centerSupply` double DEFAULT NULL,
  `centerUsage` double DEFAULT NULL,
  `southSupply` double DEFAULT NULL,
  `southUsage` double DEFAULT NULL,
  `eastSupply` double DEFAULT NULL,
  `eastUsage` double DEFAULT NULL,
  KEY `idx` (`updateTime`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `每日統計`
--

DROP TABLE IF EXISTS `每日統計`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `每日統計` (
  `測站` varchar(255) NOT NULL,
  `時間` date NOT NULL,
  `當日最高溫度` double DEFAULT NULL,
  `當日最低溫度` double DEFAULT NULL,
  `當日平均溫度` double DEFAULT NULL,
  KEY `idx` (`測站`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `逐時觀測`
--

DROP TABLE IF EXISTS `逐時觀測`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `逐時觀測` (
  `測站` varchar(255) NOT NULL,
  `時間` datetime NOT NULL,
  `測站氣壓` double DEFAULT NULL,
  `溫度` double DEFAULT NULL,
  `相對濕度` double DEFAULT NULL,
  `風速` double DEFAULT NULL,
  `風向` varchar(255) DEFAULT NULL,
  `降水量` double DEFAULT NULL,
  `日照時數` double DEFAULT NULL,
  KEY `idx` (`測站`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-10-13 19:01:14
