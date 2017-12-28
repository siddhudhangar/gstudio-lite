#!/bin/sh


    cd "$(locate -b glite-rcs-repo | fgrep -w gstudio/data/glite-rcs-repo)"

    cd Nodes

    file="./inject"

    if [ -f $file ]
    then
        
       URLS="$( find  -type f -mtime -1 -name *.json -print | xargs grep -i -r 'mimetype' | cut -d: -f1)"     

        
    for var in $URLS 
    do
        #object_id="$(echo $var | cut -d/ -f5 | cut -d. -f1)" && \
         object_id="$(echo $var | cut -d/ -f4 | cut -d. -f1)" && \
        
        mimetype[0]="application/CDFV2-corrupt"
        mimetype[1]="application/epub+zip"
        mimetype[2]="application/msword"
        mimetype[3]="application/octet-stream"
        mimetype[4]="application/pdf"
        mimetype[5]="application/vnd.geogebra.file"
        mimetype[6]="application/vnd.ms-powerpoint"
        mimetype[7]="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        mimetype[8]="application/vnd.openxmlformats-officedocument.wordprocessingml.document"        
        mimetype[9]="application/x-dosexec"
        mimetype[10]="application/x-empty"
        mimetype[11]="application/x-freemind"
        mimetype[12]="application/x-msdownload"
        mimetype[13]="application/x-rar"
        mimetype[14]="application/zip"

        mimetype[15]="audio/mpeg"
        mimetype[16]="audio/x-wav"

        mimetype[17]="image/gif"
        mimetype[18]="image/jpeg"
        mimetype[19]="image/png"
        mimetype[20]="image/svg+xml"

        mimetype[21]="video/avi"
        mimetype[22]="video/mp4"
        mimetype[23]="video/mpeg"
        mimetype[24]="video/webm"
        mimetype[25]="video/x-matroska"
        mimetype[26]="video/x-ms-asf"
        mimetype[27]="video/x-msvideo"
        
        

        for temp in ${mimetype[@]}
        do
            
                if [ "$(grep -i $temp $var | wc -l)" -gt 0 ] 
                then
                 
                 if [ $temp == "audio/mpeg" -o  $temp == "audio/x-wav" ]
                  then              
                    curl -XPOST http://10.1.0.229:9200/gstudio-lite/audios/$object_id -d @$var  
                  
            
                  elif [ $temp == "video/avi" -o  $temp == "video/mp4" -o  $temp == "video/mpeg" -o  $temp == "video/webm" -o  $temp == "video/x-matroska" -o \
                         $temp == "video/x-ms-asf" -o $temp == "video/x-msvideo" ]
                  then              
                    curl -XPOST http://10.1.0.229:9200/gstudio-lite/videos/$object_id -d @$var            
                 
                
                  elif [ $temp == "image/gif" -o  $temp == "image/jpeg" -o  $temp == "image/png" -o  $temp == "image/svg+xml" ]
                  then              
                    curl -XPOST http://10.1.0.229:9200/gstudio-lite/images/$object_id -d @$var            
                  
                  

                  elif [ $temp == "application/CDFV2-corrupt" -o  $temp == "application/epub+zip" -o  $temp == "application/msword" -o \
                      $temp == "application/pdf" -o $temp == "application/vnd.geogebra.file" -o $temp == "application/vnd.ms-powerpoint" -o \
                      $temp == "application/zip"  -o $temp == "application/vnd.openxmlformats-officedocument.presentationml.presentation" -o \
                      $temp == "application/vnd.openxmlformats-officedocument.wordprocessingml.document" -o $temp == "application/x-dosexec" -o \
                      $temp == "application/x-empty" -o $temp == "application/x-freemind" -o $temp == "application/x-msdownload" -o \
                      $temp == "application/x-rar" -o $temp == "application/zip" 	]
                  then              
                    curl -XPOST http://10.1.0.229:9200/gstudio-lite/documents/$object_id -d @$var            
                  fi
                                       
            fi
        done
    done

    else
    touch inject
    
    URLS="$(grep -i -r 'mimetype' | cut -d: -f1)"
        
    for var in $URLS 
    do
        #object_id="$(echo $var | cut -d/ -f5 | cut -d. -f1)" && \
         object_id="$(echo $var | cut -d/ -f4 | cut -d. -f1)" && \
        
        mimetype[0]="application/CDFV2-corrupt"
        mimetype[1]="application/epub+zip"
        mimetype[2]="application/msword"
        mimetype[3]="application/octet-stream"
        mimetype[4]="application/pdf"
        mimetype[5]="application/vnd.geogebra.file"
        mimetype[6]="application/vnd.ms-powerpoint"
        mimetype[7]="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        mimetype[8]="application/vnd.openxmlformats-officedocument.wordprocessingml.document"        
        mimetype[9]="application/x-dosexec"
        mimetype[10]="application/x-empty"
        mimetype[11]="application/x-freemind"
        mimetype[12]="application/x-msdownload"
        mimetype[13]="application/x-rar"
        mimetype[14]="application/zip"

        mimetype[15]="audio/mpeg"
        mimetype[16]="audio/x-wav"

        mimetype[17]="image/gif"
        mimetype[18]="image/jpeg"
        mimetype[19]="image/png"
        mimetype[20]="image/svg+xml"

        mimetype[21]="video/avi"
        mimetype[22]="video/mp4"
        mimetype[23]="video/mpeg"
        mimetype[24]="video/webm"
        mimetype[25]="video/x-matroska"
        mimetype[26]="video/x-ms-asf"
        mimetype[27]="video/x-msvideo"
        
        

        for temp in ${mimetype[@]}
        do
            
                if [ "$(grep -i $temp $var | wc -l)" -gt 0 ] 
                then
                 
                 if [ $temp == "audio/mpeg" -o  $temp == "audio/x-wav" ]
                  then              
                    curl -XPOST http://10.1.0.229:9200/gstudio-lite/audios/$object_id -d @$var  
                  
            
                  elif [ $temp == "video/avi" -o  $temp == "video/mp4" -o  $temp == "video/mpeg" -o  $temp == "video/webm" -o  $temp == "video/x-matroska" -o \
                         $temp == "video/x-ms-asf" -o $temp == "video/x-msvideo" ]
                  then              
                    curl -XPOST http://10.1.0.229:9200/gstudio-lite/videos/$object_id -d @$var            
                 
                
                  elif [ $temp == "image/gif" -o  $temp == "image/jpeg" -o  $temp == "image/png" -o  $temp == "image/svg+xml" ]
                  then              
                    curl -XPOST http://10.1.0.229:9200/gstudio-lite/images/$object_id -d @$var            
                  
                  

                  elif [ $temp == "application/CDFV2-corrupt" -o  $temp == "application/epub+zip" -o  $temp == "application/msword" -o \
                      $temp == "application/pdf" -o $temp == "application/vnd.geogebra.file" -o $temp == "application/vnd.ms-powerpoint" -o \
                      $temp == "application/zip"  -o $temp == "application/vnd.openxmlformats-officedocument.presentationml.presentation" -o \
                      $temp == "application/vnd.openxmlformats-officedocument.wordprocessingml.document" -o $temp == "application/x-dosexec" -o \
                      $temp == "application/x-empty" -o $temp == "application/x-freemind" -o $temp == "application/x-msdownload" -o \
                      $temp == "application/x-rar" -o $temp == "application/zip" 	]
                  then              
                    curl -XPOST http://10.1.0.229:9200/gstudio-lite/documents/$object_id -d @$var            
                  fi
                                       
            fi
        done
    done
fi


