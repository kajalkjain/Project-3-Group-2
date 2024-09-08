-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/1Tl3sA
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


-- Patient table
CREATE TABLE "Patient_Table" (
    "PatientID" int   NOT NULL,
    "First_name" varchar(100)   NOT NULL,
    "Last_name" varchar(100)   NOT NULL,
    "Age" int   NOT NULL,
    "Gender" varchar(10)   NOT NULL,
    "Blood_Type" varchar(5)   NOT NULL,
    "Medical_Condition" varchar(100)   NOT NULL,
    CONSTRAINT "pk_Patient_Table" PRIMARY KEY (
        "PatientID"
     )
);

-- Admission table
CREATE TABLE "Admission_Table" (
    "AdmissionID" int   NOT NULL,
    "PatientID" int   NOT NULL,
    "Date_of_Admission" date   NOT NULL,
    "Doctor" varchar(100)   NOT NULL,
    "Hospital" varchar(100)   NOT NULL,
    "Insurance_Provider" varchar(500)   NOT NULL,
    "Billing_Amount" decimal   NOT NULL,
    "Room_Number" int   NOT NULL,
    "Admission_Type" varchar(50)   NOT NULL,
    "Discharge_Date" date   NOT NULL,
    CONSTRAINT "pk_Admission_Table" PRIMARY KEY (
        "AdmissionID"
     )
);

-- Medication table
CREATE TABLE "Medication_Table" (
    "MedicationID" int   NOT NULL,
    "AdmissionID" int   NOT NULL,
    "Medication" varchar(50)   NOT NULL,
    CONSTRAINT "pk_Medication_Table" PRIMARY KEY (
        "MedicationID"
     )
);

-- Test Results table
CREATE TABLE "Test_Results_Table" (
    "TestResultID" int   NOT NULL,
    "AdmissionID" int   NOT NULL,
    "Test_Results" varchar(100)   NOT NULL,
    CONSTRAINT "pk_Test_Results_Table" PRIMARY KEY (
        "TestResultID"
     )
);

ALTER TABLE "Admission_Table" ADD CONSTRAINT "fk_Admission_Table_PatientID" FOREIGN KEY("PatientID")
REFERENCES "Patient_Table" ("PatientID");

ALTER TABLE "Medication_Table" ADD CONSTRAINT "fk_Medication_Table_AdmissionID" FOREIGN KEY("AdmissionID")
REFERENCES "Admission_Table" ("AdmissionID");

ALTER TABLE "Test_Results_Table" ADD CONSTRAINT "fk_Test_Results_Table_AdmissionID" FOREIGN KEY("AdmissionID")
REFERENCES "Admission_Table" ("AdmissionID");

