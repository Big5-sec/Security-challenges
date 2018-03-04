push_E   	   	 	
print	
  push_n   		 			 
print	
  push_t   			 	  
print	
  push_e   		  	 	
print	
  push_r   			  	 
print	
  push_espace    	     
print	
  push_1   	
push_c   		   		
store		 push_2   	 
push_1    		   	
store		 push_3   		
push_1    		   	
store		 push_t   			 	  
print	
  push_h   		 	   
print	
  push_e   		  	 	
print	
  push_espace    	     
print	
  push_4   	  
push_c   		   		
store		 push_5   	 	
push_2    		  	 
store		 push_f   		  		 
print	
  push_l   		 		  
print	
  push_6   		 
push_4    		 	  
store		 push_a   		    	
print	
  push_7   			
push_4    		 	  
store		 push_g   		  			
print	
  push_(    	 	   
print	
  push_8   	   
push_8    			   
store		 push_b   		   	 
print	
  push_9   	  	
push_c   		   		
store		 push_y   				  	
print	
  push_espace    	     
print	
  push_c   		   		
print	
  push_h   		 	   
print	
  push_10   	 	 
push_1    		   	
store		 push_11   	 		
push_1    		   	
store		 push_a   		    	
print	
  push_r   			  	 
print	
  push_,    	 		  
print	
  push_z   				 	 
print	
  push_espace    	     
print	
  push_t   			 	  
print	
  push_o   		 				
print	
  push_espace    	     
print	
  push_12   		  
push_c   		   		
store		 push_f   		  		 
print	
  push_i   		 	  	
print	
  push_n   		 			 
print	
  push_i   		 	  	
print	
  push_s   			  		
print	
  push_h   		 	   
print	
  push_)    	 	  	
print	
  push_:    			 	 
print	
  push_nl      	 	 
dup 
 print	
  print	
  storeforcharloop_push_20   	 	  
push_c   		   		
store		 push_21   	 	 	
push_h   		 	   
store		 push_22   	 		 
push_a   		    	
store		 push_23   	 			
push_r   			  	 
store		 push_24   		   
push_:    			 	 
store		 push_25   		  	
push_00   
store		 push_index_30   				 
push_01   	
store		 push_resultat_31   					
push_00   
store		 label_1tab
  	
push_20_for_retrieve   	 	  
label_2tab
  		
dup_stack 
 heap_retrieve			dup_stack 
 jz_label3tab
	 			
output_car	
  push_1   	
add	   jump_label2tab
 
		
label3tab
  			
discard 

push_50   		  	 
read_char	
	 push_50   		  	 
retrieve_char			dup 
 push_z   				 	 
sub	  	jz_label5tab
	 					
push_1   	
add	   push_index_addr_30   				 
retrieve_index			dup 
 push_1   	
add	   push_index_addr_30   				 
swap 
	store_index		 retrieve_flag_index			sub_equal	  	jz_label4tab
	 				
push_resultat_addr_31   					
retrieve_resultat			push_1   	
add	   push_addr_resultat_31   					
swap 
	store_result		 label4tab
  				
push_50   		  	 
read_char	
	 jump_label1tab
 
	
label5tab
  					
push_addr_index_30   				 
retrieve_index			push_13   		 	
sub	  	jz_label8tab
	 								
jump_label9
 
									
label8tab
  								
push_addr_resultat_31   					
retrieve_resultat			jz_label7tab
	 							
label9_tab
  									
push_B   	    	 
print	
  push_a   		    	
print	
  push_d   		  	  
print	
  push_espace    	     
print	
  push_f   		  		 
print	
  push_l   		 		  
print	
  push_a   		    	
print	
  push_g   		  			
print	
  jump_label6tab
 
						
label7tab
  							
push_G   	   			
print	
  push_o   		 				
print	
  push_o   		 				
print	
  push_d   		  	  
print	
  push_espace    	     
print	
  push_f   		  		 
print	
  push_l   		 		  
print	
  push_a   		    	
print	
  push_g   		  			
print	
  label6tab
  						
end



