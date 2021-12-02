import java.io.*;
public class Student {
   String name;
   int age;
   double mark;
 
   public Student(String name) {
      this.name = name;
   }

   public void stuAge(int stuAge) {
      age = stuAge;
   }




   public void stuMark(double stuMark) {
      mark = stuMark;
   }

   public void printStudent() {
      System.out.println("Name:"+ name );
      System.out.println("Age:" + age );
      System.out.println("Mark:" + mark);
   }
}