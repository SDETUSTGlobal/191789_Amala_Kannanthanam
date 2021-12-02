package com.app.Mockito;

import static org.hamcrest.CoreMatchers.is;  
import static org.junit.Assert.*;  
import static org.mockito.BDDMockito.given;  
import static org.mockito.Mockito.mock;  
import static org.mockito.Mockito.when;  
  
import java.util.List;  
import org.junit.Test;  
import org.mockito.Mockito;  
  
public class TestListtri1{  
  
            @Test  
    public void testList_usingBDD() {  
           
      //Given - setup part  
  
      List<String> mocklist = mock(List.class);  
      given(mocklist.get(Mockito.anyInt())).willReturn("Mockito");  
        
      //When - invocation   
      String string1 = mocklist.get(0);  
        
      //Then - readable assert  
      assertThat(string1, is("Mockito"));  
     }  
  }  
