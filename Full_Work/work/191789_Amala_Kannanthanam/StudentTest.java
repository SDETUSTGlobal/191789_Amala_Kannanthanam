import java.io.*;
public class StudentTest {

   public static void main(String args[]) {
     
      Student stuOne = new Student("Amala B");
	  Student stuTwo = new Student("Alka Varghese");
	  Student stuThree = new Student("Sivakarthik");
    

     
      stuOne.stuAge(20);
	  stuOne.stuMark(100);
	  stuOne.printStudent();
	  
	  stuTwo.stuAge(21);
	  stuTwo.stuMark(99);
	  stuTwo.printStudent();
	  
	  stuThree.stuAge(19);
	  stuThree.stuMark(98);
	  stuThree.printStudent();
	  
      

     
   }
}