public class Ob extends Exception{  
 int d=500,d2=300;

 static int c1=0;
 public Ob(String s)
 {
    super(s);
 }
  
  
 void ch(Ob op){  
 op.d=op.d+10;
 }  
     void ch1(int data){  
 d2=d2+10;
 }  
static void rec() throws Ob{    
         
            
       c1++;
        if(c1>3)
           {throw new Ob("c1  greater than 3");  } 
       else
        {System.out.println(c1);  }
        
         rec();
        }
    
 public static void main(String args[])
 throws ClassNotFoundException
    {
 try {
           
           Class temp=Class.forName("Ob");
           int b=30; 
Integer j=Integer.valueOf(b);

System.out.println(b+" "+j);  
            }
        catch (ClassNotFoundException e) {
           
            System.out.println(
                "Class does not exist");
        }
     
   Ob op=new Ob("c1  less than 3");  
 
   System.out.println("before  "+op.d);  
   op.ch(op);
   System.out.println("after  "+op.d);  
   System.out.println("before  "+op.d2);  
   op.ch1(500);  
   System.out.println("after  "+op.d2);  
    
   int a[]={33,3,4,5};
for(int i=0;i<a.length;i++)
System.out.println(a[i]);  
try{
System.out.println(a[2]/0);
}catch(ArithmeticException e){System.out.println(e);}  
    
 try{
rec();
}
catch( Ob ex)  
        {  
            System.out.println("Catched the exception");  
     System.out.println("Exception: " + ex);  
        }  

   
  
 }  
}  