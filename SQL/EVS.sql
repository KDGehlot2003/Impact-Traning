CREATE TABLE EVS_TBL_User_Credentials(
	Userid varchar(6) PRIMARY KEY,
	Password varchar(20) NOT NULL,
	Usertype varchar(1) CHECK(Usertype='A' OR Usertype='E' OR Usertype='V'),
	Loginstatus INT(1) CHECK(Loginstatus='1' OR Loginstatus='0'));

CREATE TABLE EVS_TBL_User_Profile(
	Userid VARCHAR(6),
	Firstname VARCHAR(15) NOT NULL,
	Lastname VARCHAR(15) NOT NULL,
	Dateofbirth DATE NOT NULL,
	Gender VARCHAR(7) NOT NULL,
	Street VARCHAR(30) NOT NULL,
	Location VARCHAR(15) NOT NULL,
	City VARCHAR(15) NOT NULL,
	State VARCHAR(15) NOT NULL,
	Pincode VARCHAR(10) NOT NULL,
	MobileNo VARCHAR(10) NOT NULL,
	EmailId VARCHAR(30),
	FOREIGN KEY(Userid) REFERENCES EVS_TBL_User_Credentials(Userid));

CREATE TABLE EVS_TBL_Election (
	ElectionId VARCHAR(6) PRIMARY KEY, 
	Name VARCHAR(15) NOT NULL, 
	Electiondate DATE NOT NULL, 
	District VARCHAR(15) NOT NULL, 
	Constituency VARCHAR(15) NOT NULL, 
	Countingdate DATE NOT NULL);

CREATE TABLE EVS_TBL_Party ( 
	PartyId VARCHAR(6) PRIMARY KEY, 
	Name VARCHAR(20) NOT NULL, 
	Leader VARCHAR(20) NOT NULL, 
	Symbol VARCHAR(60) default '/Users/macbook/Desktop/Impact Traning/SQL');

CREATE TABLE EVS_TBL_Candidate(
	CandidateId VARCHAR(6) PRIMARY KEY,
	Name VARCHAR(20) NOT NULL,
	ElectionId VARCHAR(6),
	PartyId VARCHAR(6),
	District VARCHAR(20) NOT NULL,
	Constituency VARCHAR(20) NOT NULL,
	Dateofbirth DATE NOT NULL,
	MobileNo VARCHAR(10),
	Address VARCHAR(50) NOT NULL,
	EmailId VARCHAR(20),
	FOREIGN KEY(ElectionId) REFERENCES EVS_TBL_Election(ElectionId),
	FOREIGN KEY(PartyId) REFERENCES EVS_TBL_Party(PartyId));

CREATE TABLE EVS_TBL_Application (
	UserId VARCHAR(6), 
	Constituency VARCHAR(20) NOT NULL, 
	Passedstatus INT(2) CHECK(Passedstatus='1' OR Passedstatus='2' OR Passedstatus='3'), 
	Approvedstatus INT(2) CHECK(Approvedstatus='0' OR Approvedstatus='1'), 
	VoterId VARCHAR(8) PRIMARY KEY, 
	FOREIGN KEY(UserId) REFERENCES EVS_TBL_User_Credentials(UserId));

CREATE TABLE EVS_TBL_Result(
	Serialno int(6) PRIMARY KEY AUTO_INCREMENT,
	Electionid VARCHAR(6),
	Candidateid VARCHAR(6),
	Votecount int(5) NOT NULL,
	FOREIGN KEY(Electionid) REFERENCES EVS_TBL_Election(Electionid),
	FOREIGN KEY(Candidateid) REFERENCES EVS_TBL_Candidate(Candidateid));

CREATE TABLE EVS_TBL_EO(
	Electionofficerid VARCHAR(6) PRIMARY KEY,
	Constituency VARCHAR(25) NOT NULL);

CREATE TABLE EVS_TBL_Voter_Details ( 
	Serialno INT(6) PRIMARY KEY AUTO_INCREMENT, 
	Candidateid VARCHAR(6), 
	Electionid VARCHAR(6), 
	Voterid VARCHAR(8), 
	FOREIGN KEY(Candidateid) REFERENCES EVS_TBL_Candidate(Candidateid), 
	FOREIGN KEY(Electionid) REFERENCES EVS_TBL_Election(Electionid), 
	FOREIGN KEY(Voterid) REFERENCES EVS_TBL_Application(VoterId));