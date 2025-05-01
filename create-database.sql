CREATE DATABASE LegalClinic;

CREATE USER LegalClinic_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE LegalClinic TO LegalClinic_admin;
