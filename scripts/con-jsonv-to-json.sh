
#!/bin/sh

	cd "$(locate -b rcs-repo | fgrep -w gstudio/data/rcs-repo)"
	

	file="./ref"
	
	if [ -f $file ]
	then
		#echo "file found"
        
         #cd "$(locate -b rcs-repo | fgrep -w gstudio/data/rcs-repo)"  

    if [ "$( find . -name '*json,v' | find  -type f -mtime -1 -print | wc -l)" -gt 0 ]
    then
    
    mkdir -p ../glite-rcs-repo 
    
    cd ../glite-rcs-repo   

    cd ../rcs-repo 

        TEMP1="$(find . -name '*json,v' | find  -type f -mtime -1)"

        for file_name  in  $TEMP1
        do
            TEMP="$(find $file_name | cut -d/ -f2-5)" 
        
            cd ../glite-rcs-repo && \
    
            mkdir -p $TEMP && \
            
            cd $TEMP 
            
            file_name1="$(echo $file_name | cut -c 2-)"        

            rcs co ../../../../../rcs-repo$file_name1 && \

            TEMP2="$(echo $file_name1 | cut -d/ -f6-)"	
                
		    v1=$TEMP2

		    v2=${v1::-2}
			
            sed -i -e 's/_id/id/g' -e 's/_type/type/g' $v2 && \

            cd ../../../../ && \
    
            cd ../rcs-repo
      
        done

    fi
    
	else
		#echo "file not found"	
        apt-get install rcs
    touch ref
                                        
    #cd "$(locate -b rcs-repo | fgrep -w gstudio/data/rcs-repo)"  
  

    if [ "$(find . -name "*.json,v" -type f | wc -l)" -gt 0 ] 
    then   

        if [ "$(find . -name "*.json,v"  | cut -d/ -f2 | sort | uniq | wc -l)" -gt 0 ] 
        then     
        
            mkdir -p ../glite-rcs-repo 
    
            cd ../glite-rcs-repo   

            cd ../rcs-repo     
  
            TEMP1="$(find . -name '*.json,v')"
            for file_name  in  $TEMP1
            do          

                    TEMP="$(find $file_name | cut -d/ -f2-5)"   

                    cd ../glite-rcs-repo && \
    
                    mkdir -p $TEMP && \
            
                    cd $TEMP    
                       
                    file_name1="$(echo $file_name | cut -c 2-)"        

                    rcs co -u ../../../../../rcs-repo$file_name1 

		            TEMP2="$(echo $file_name1 | cut -d/ -f6-)"	
                
		            v1=$TEMP2

		            v2=${v1::-2}
			
                    sed -i -e 's/_id/id/g' -e 's/_type/type/g' $v2 && \

                    cd ../../../../ && \
    
                    cd ../rcs-repo     
            done
        fi

    fi
        
	fi
