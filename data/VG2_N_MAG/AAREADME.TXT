PDS_VERSION_ID       = PDS3                                                  
RECORD_TYPE          = STREAM                                                
                                                                             
^TEXT                = "AAREADME.TXT"                                        
OBJECT               = TEXT                                                  
  PUBLICATION_DATE   = 2011-06-02                                            
  NOTE               = "AAREADME.TXT describes this volume."                 
END_OBJECT           = TEXT                                                  
END                                                                          
                                                                             
              Voyager 2 at Neptune VG2-N-MAG-4-RDR-HGCOORDS-1.92SEC-V1.0     
                                                                             
                        1989-08-22 to 1989-08-29                             
                                                                             
Introduction                                                                 
============                                                                 
                                                                             
This volume contains data recorded during the Voyager 2 Neptune Encounter and
submitted to the Planetary Data System (PDS) by Voyager MAG investigators.   
                                                                             
Data that may appear on this volume as version 1.1 was previously archived   
with the NSSDC and PDS as version 1.0. Changes include reformatting of the   
time column, standardization of flag values, and upgrading of labels and     
catalog templates to PDS version 3.2. Data found on this volume supersede    
all previous versions.                                                       
                                                                             
Every effort has been made to insure that the data are of the best quality   
available. However, the PDS and the Planetary Plasma Interactions (PPI) Node 
in particular, assume no liability for this volume or its contents. Users are
encouraged to verify the 'correctness' of the data prior to submitting any   
publications or other work based on these data.                              
                                                                             
Brief Volume Description                                                     
----------------------                                                       
                                                                             
This data set is organized into 5 principal sub-directories:                 
                                                                             
  CATALOG   PDS catalog templates describing the Voyager mission,            
            spacecraft, instruments, data sets, key personnel and references 
                                                                             
  DATA      science data from the MAG (Fluxgate Magnetometer) instrument     
                                                                             
  DOCUMENT  documents describing instruments, data sets, or software         
            contained on this volume                                         
                                                                             
  INDEX     index of all user files contained on this volume                 
                                                                             
  EXTRAS    additional information                                           
                                                                             
                                                                             
More information on directory structure is contained in the section entitled 
'Volume Contents and Structure.' Novice users, however, may ignore all files 
and directories except for the 'Important Files and Directories' listed      
below.                                                                       
                                                                             
Important Files and Directories                                              
-------------------------------                                              
                                                                             
All data files are stored, either in ASCII (.TAB) or binary (.DAT) format    
files, in the /DATA branch of the directory tree. The content of each data   
file is described by a detached PDS label file (.LBL). A single format file  
(.FMT), which is pointed to by the label file (^STRUCTURE), describes the    
data file's internal structure or record format. The files DATASET.TXT and   
INFO.TXT provide additional information about data set and directory         
contents.                                                                    
                                                                             
An *INFO.TXT file (e.g. CATINFO.TXT, etc.), containing a description of the  
directory tree and sub-directory contents, is located in every directory     
immediately below the root. The INFO.TXT files provided on selected data     
sub-directories contain detailed descriptions of the directories on which    
they are located.                                                            
                                                                             
Documents                                                                    
=========                                                                    
                                                                             
The documents provided on this volume (in the /DOCUMENT sub-directory)       
include copyrighted materials previously published in Space Science Reviews, 
Vol. 21, No. 2, pp. 77-101, November 1977, and Space Science Reviews,        
Vol. 21, No. 3, pp. 235-376, December 1977. These materials appear on this   
volume with the permission of Kluwer Academic Publications (Kluwer). Kluwer  
retains Copyright over these articles. Please see the Copyright statement    
appearing at the beginning of each of the Space Science Reviews articles.    
                                                                             
                                                                             
File Formats                                                                 
============                                                                 
                                                                             
All of the label, table, and text files are ASCII format.                    
                                                                             
All files in this volume are described by detached or combined detached PDS  
labels. PDS labels have a file extension of '.LBL' and generally have the    
same name as the file which it describes. All PDS label files in this volume 
are completely PDS Standards Version 3.8 compliant.                          
                                                                             
Data files are either stored in ASCII (.TAB), or binary (.DAT) format. ASCII 
file records are generally fixed length with space delimited                 
fields or columns. Refer to the label (.LBL) and format (.FMT) files for     
information about the format and structure of a specific data file.          
                                                                             
This volume contains copies of documents associated with the data provided.  
These documents are reproduced in both plain ASCII text (.ASC) and PDF(.PDF) 
versions.                                                                    
                                                                             
                                                                             
Errata                                                                       
======                                                                       
                                                                             
For a description of any errors known at the time of the production of this  
volume, please refer to the file ERRATA.TXT found in the root directory.     
                                                                             
                                                                             
Volume Contents and Structure                                                
=============================                                                
                                                                             
The tree diagram below provides a listing and brief description of the       
contents and key files of the root directory and instrument sub-directories  
of the /DATA directory. Note that some files may be omitted from this        
description. Each file in this volume (with the exception of *.CAT files) is 
associated with a PDS label file (.LBL) which describes its content and      
characteristics. For more information, please refer to the *INFO.TXT files   
located on each of the sub-directories of the root directory, or the         
INFO.TXT files located on the individual data sub-directories.               
                                                                             
Square brackets ([]) denote directories.                                     
                                                                             
   VG2_9048 (root directory)                                                 
     |                                                                       
     |- AAREADME.TXT  describes volume contents and organization (this file) 
     |                                                                       
     |- ERRATA.TXT    file describing errors and anomalies found in this     
     |                volume                                                 
     |                                                                       
     |- VOLDESC.CAT   high level description of volume contents              
     |                                                                       
     |-[CATALOG]      Contains metadata associated with this volume including
     |                mission, instrument host (spacecraft), instrument,     
     |                data set, personnel and reference descriptions and     
     |                information (*.CAT files)                              
     |                                                                       
     |-[DOCUMENT]     Contains mission, software, and instrument             
     |                sub-directories which contain documents relating to    
     |                the data set.                                          
     |                                                                       
     |-[INDEX]        Contains a listing including file name and location,   
     |                for all user files contained in this volume.           
     |                                                                       
     |-[EXTRAS]       Bonus content not necessarily conforming to            
     |                PDS archive standards.                                 
                                                                             
     |-[DATA]         Contains Voyager 2 1.92 second resampled data in       
                      Heliographic coordinates from the Low Field            
                      Magnetometer (LFM) from Voyager 2 during the           
                      Neptune encounter                                      
                                                                             
Contacts                                                                     
========                                                                     
                                                                             
The person most directly responsible for the construction and release of     
this volume is Mr. Steven Joy. He was the PPI Node Data Administrator at the 
time this volume was created and understands as much about the structure     
and data organization as anyone. The construction of the PDS labels and      
templates was done by Mr. Joe Mafi. Other PPI personnel who may be aware of  
about issues related to this volume include Dr. Raymond Walker, the PDS/PPI  
node manager.                                                                
                                                                             
For questions or problems regarding this Clime, please contact the PDS/PPI   
PDS operator:                                                                
                                                                             
  Email             pds_operator@igpp.ucla.edu                               
                                                                             
  Telephone         (310) 206-6073                                           
                                                                             
  U.S. Mail         PDS Operator                                             
                    c/o Dr. Raymond Walker                                   
                    3845 Slichter Hall                                       
                    UCLA - IGPP                                              
                    Los Angeles, CA 90095-156704                             
                                                                             
For questions regarding PDS Standards or other volumes available from PDS,   
please contact PDS Operator at the PDS Central Node (at JPL):                
                                                                             
  Email             pds_operator@jpl.nasa.gov                                
                                                                             
  Telephone         (818) 354-4321                                           
                                                                             
  U.S. Mail         Planetary Data System, PDS Operator                      
                    Jet Propulsion Laboratory                                
                    4800 Oak Grove Drive                                     
                    Mail Stop 202-101                                        
                    Pasadena, CA 91109                                       
                                                                             
