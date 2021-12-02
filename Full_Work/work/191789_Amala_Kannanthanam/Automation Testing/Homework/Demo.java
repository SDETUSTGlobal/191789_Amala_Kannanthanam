package sel1;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.DesiredCapabilities;  
import org.openqa.selenium.support.ui.Select;  
public class Demo {

	public static void main(String[] args) {
		
System.setProperty("webdriver.chrome.driver","D://Software//SEL_JAR-20210901T092836Z-001//SEL_JAR//chromedriver_win32//chromedriver.exe");
		DesiredCapabilities capabilities = DesiredCapabilities.chrome();  
		capabilities.setCapability("marionette",true);
		WebDriver driver = new ChromeDriver();
		driver.manage().window().maximize();
		
		driver.navigate().to("http://secure.smartbearsoftware.com/samples/testcomplete11/WebOrders/login.aspx");
		 String sampleText = driver.findElement(By.className("info")).getText();  //classname
	     System.out.println(sampleText);  
	          
		
		driver.findElement(By.id("ctl00_MainContent_username")).sendKeys("Tester");
		driver.findElement(By.id("ctl00_MainContent_password")).sendKeys("test");
		driver.findElement(By.id("ctl00_MainContent_login_button")).click();
		driver.findElement(By.id("ctl00_MainContent_btnCheckAll")).click();
		
	
		driver.findElement(By.id("ctl00_MainContent_btnDelete")).click();
		driver.findElement(By.id("ctl00_MainContent_orderLInk")).click();
		driver.navigate().back();
		driver.navigate().back();
		driver.findElement(By.id("ctl00_MainContent_btnUncheckAll")).click();
		driver.findElement(By.id("ctl00_MainContent_orderGrid_ctl02_OrderSelector")).click();
		driver.findElement(By.id("ctl00_MainContent_btnUncheckAll")).click();
		 String sample = driver.findElement(By.tagName("h2")).getText();  //tagname
	     System.out.println(sample); 
		
		
	
		driver.findElement(By.linkText("View all products")).click();//linktext
		driver.findElement(By.partialLinkText("Order")).click();//partiallinktext
		
		Select dropdown = new Select(driver.findElement(By.id("ctl00_MainContent_fmwOrder_ddlProduct")));  
	    dropdown.selectByVisibleText("FamilyAlbum");  
	  
	    driver.findElement(By.cssSelector("#ctl00_MainContent_fmwOrder_txtQuantity")).sendKeys("1000");//css Selector
	    driver.findElement(By.id("ctl00_MainContent_fmwOrder_txtUnitPrice")).sendKeys("80");//id
		driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]")).click();//xpath
		
		driver.findElement(By.name("ctl00$MainContent$fmwOrder$txtName")).sendKeys("Amala");//name
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox2")).sendKeys("manimala");

		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox3")).sendKeys("kottayam");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox4")).sendKeys("Kerala");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox5")).sendKeys("686543");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_cardList_0")).click();
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox6")).sendKeys("123456789012");
		   driver.findElement(By.id("ctl00_MainContent_fmwOrder_TextBox1")).sendKeys("01/99");
		   driver.findElement(By.xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/div/a")).click();
		   Select drop = new Select(driver.findElement(By.id("ctl00_MainContent_fmwOrder_ddlProduct")));  
		    drop.selectByVisibleText("ScreenSaver");  
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
