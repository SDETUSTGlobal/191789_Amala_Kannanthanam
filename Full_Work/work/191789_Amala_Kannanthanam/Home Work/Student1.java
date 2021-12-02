
class Student{  
   int rollno;
   String name;  
   static String college ="MITS"; 
     
   Student(int roll, String n){  
   rollno = roll;  
   name = n;  
   }  
     
   void display (){System.out.println(rollno+" "+name+" "+college);}  
}  
  
public class Student1{  
 public static void main(String args[]){  
 Student a1 = new Student(1,"ANN");  
 Student a2 = new Student(2,"AMALA");  
 Student a3 = new Student(3,"AlISHA");  
 Student a4 = new Student(4,"ARYA");  
 Student a5 = new Student(5,"ABHII");  
 
 
 a1.display(); 
 a2.display(); 
 a3.display(); 
 a4.display();  
 a5.display(); 

 }  
}  
