-- MySQL dump 10.13  Distrib 8.0.36, for macos14 (arm64)
--
-- Host: localhost    Database: assignments
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `EVS_TBL_Application`
--

DROP TABLE IF EXISTS `EVS_TBL_Application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EVS_TBL_Application` (
  `UserId` varchar(6) DEFAULT NULL,
  `Constituency` varchar(20) NOT NULL,
  `Passedstatus` int DEFAULT NULL,
  `Approvedstatus` int DEFAULT NULL,
  `VoterId` varchar(8) NOT NULL,
  PRIMARY KEY (`VoterId`),
  KEY `UserId` (`UserId`),
  CONSTRAINT `evs_tbl_application_ibfk_1` FOREIGN KEY (`UserId`) REFERENCES `EVS_TBL_User_Credentials` (`Userid`),
  CONSTRAINT `evs_tbl_application_chk_1` CHECK (((`Passedstatus` = _utf8mb4'1') or (`Passedstatus` = _utf8mb4'2') or (`Passedstatus` = _utf8mb4'3'))),
  CONSTRAINT `evs_tbl_application_chk_2` CHECK (((`Approvedstatus` = _utf8mb4'0') or (`Approvedstatus` = _utf8mb4'1')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EVS_TBL_Application`
--

LOCK TABLES `EVS_TBL_Application` WRITE;
/*!40000 ALTER TABLE `EVS_TBL_Application` DISABLE KEYS */;
/*!40000 ALTER TABLE `EVS_TBL_Application` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-05  8:48:24
