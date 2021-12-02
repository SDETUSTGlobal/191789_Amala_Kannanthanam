
package sel1;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.DesiredCapabilities;  
import org.openqa.selenium.support.ui.Select;  
public class Demo1{

	public static void main(String[] args) {
		
System.setProperty("webdriver.chrome.driver","D://Software//SEL_JAR-20210901T092836Z-001//SEL_JAR//chromedriver_win32//chromedriver.exe");
		DesiredCapabilities capabilities = DesiredCapabilities.chrome();  
		capabilities.setCapability("marionette",true);
		WebDriver driver = new ChromeDriver();
		driver.manage().window().maximize();
		
		driver.navigate().to("http://secure.smartbearsoftware.com/samples/testcomplete11/WebOrders/login.aspx");
		 String sampleText = driver.findElement(By.className("info")).getText();  
	     System.out.println(sampleText);  
	          
		
		driver.findElement(By.id("ctl00_MainContent_username")).sendKeys("Tester");
	    
	     
		driver.findElement(By.id("ctl00_MainContent_password")).sendKeys("test");
		
		driver.findElement(By.id("ctl00_MainContent_login_button")).click();
		
		 String sam = driver.findElement(By.xpath("//*[@id='ctl00_MainContent_orderGrid']/tbody/tr[3]/td[4]")).getText(); 
	     System.out.println("No of sold family Album in canada:" +sam); //qn2 part1
	     String rowtext=driver.findElement(By.xpath("//*[@id='ctl00_MainContent_orderGrid']/tbody/tr[3]")).getText();
			System.out.println("value is:"+rowtext);
			List  rows = driver.findElements(By.xpath("//*[@id='ctl00_MainContent_orderGrid']/tbody/tr")); //qn 2 part 2
			System.out.println("No of rows are : " + rows.size());
			int c=0;
		  for(int i=3;i<rows.size();i++)
		  {   
			  String text=driver.findElement(By.xpath("//*[@id='ctl00_MainContent_orderGrid']/tbody/tr["+(i)+"]/td[3]")).getText();
			  String text2=driver.findElement(By.xpath("//*[@id='ctl00_MainContent_orderGrid']/tbody/tr["+(i)+"]/td[10]")).getText();
			if(text.equals("MyMoney") && text2.equals("MasterCard"))
			{
				 				
				 
				
				 
					 c=c+1;
				 
				
			}
			
		  }
		  System.out.println("Count : " + c);

	   
		driver.findElement(By.partialLinkText("Order")).click();
		
		Select dropdown = new Select(driver.findElement(By.id("ctl00_MainContent_fmwOrder_ddlProduct")));  
	    dropdown.selectByVisibleText("FamilyAlbum");  //qn 1 part1 by visible Text
	  
	    driver.findElement(By.cssSelector("#ctl00_MainContent_fmwOrder_txtQuantity")).sendKeys("1000");
	    driver.findElement(By.id("ctl00_MainContent_fmwOrder_txtUnitPrice")).sendKeys("80");
		driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]")).click();
		
		driver.findElement(By.name("ctl00$MainContent$fmwOrder$txtName")).sendKeys("Amala");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox2")).sendKeys("manimala");

		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox3")).sendKeys("kottayam");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox4")).sendKeys("Kerala");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox5")).sendKeys("686543");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_cardList_0")).click();
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox6")).sendKeys("123456789012");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox1")).sendKeys("01/99");
		   driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/div/a")).click();
		   Select drop = new Select(driver.findElement(By.id("ctl00_MainContent_fmwOrder_ddlProduct")));  
		    drop.selectByValue("ScreenSaver");  //qn 1 part 2 byvalue
		    driver.findElement(By.id("ctl00_MainContent_fmwOrder_txtQuantity")).sendKeys("1000");
		    driver.findElement(By.id("ctl00_MainContent_fmwOrder_txtUnitPrice")).sendKeys("80");
			driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]")).click();
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_txtName")).sendKeys("Amala");
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox2")).sendKeys("manimala");
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox3")).sendKeys("kottayam");
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox4")).sendKeys("Kerala");
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox5")).sendKeys("686543");
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_cardList_0")).click();
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox6")).sendKeys("123456789012");
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox1")).sendKeys("01/99");
		   driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/div/input")).click();
		  
		   Select dro = new Select(driver.findElement(By.id("ctl00_MainContent_fmwOrder_ddlProduct")));  
		    dro.selectByIndex(0);  // qn 1 part 3 byindex
		  driver.findElement(By.id("ctl00_MainContent_fmwOrder_txtQuantity")).sendKeys("1000");
		    driver.findElement(By.id("ctl00_MainContent_fmwOrder_txtUnitPrice")).sendKeys("80");
			driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]")).click();
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_txtName")).sendKeys("Amala");
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox2")).sendKeys("manimala");
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox3")).sendKeys("kottayam");
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox4")).sendKeys("Kerala");
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox5")).sendKeys("686543");
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_cardList_0")).click();
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox6")).sendKeys("123456789012");
			   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox1")).sendKeys("01/99");
		   driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/div/input")).click();
		  
		driver.close();
	}

}
