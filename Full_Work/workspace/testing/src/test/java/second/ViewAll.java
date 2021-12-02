package second;
import org.openqa.selenium.By;  
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;  
import cucumber.annotation.en.Given;  
import cucumber.annotation.en.Then;  
import cucumber.annotation.en.When;    
public class ViewAll {
	WebDriver driver= null;
	  @Given("^I am on user login page$")  
	  public void goToWebLogin() {  
	  
	  System.setProperty("webdriver.chrome.driver", "D://eclipse1//Sel_jar//chromedriver_win32//chromedriver.exe");
	  driver= new ChromeDriver();
	  driver.navigate().to("http://secure.smartbearsoftware.com/samples/TestComplete11/WebOrders/Default.aspx");  
	  }  
	     
	  @When("^I enter valid data on the page$")  
	  public void enterData(){ 
		//driver.findElement(By.id("ctl00_MainContent_username")).sendKeys("Tester");
		//driver.findElement(By.id("ctl00_MainContent_password")).sendKeys("test");
		//driver.findElement(By.id("ctl00_MainContent_login_button")).click();
		driver.findElement(By.id("ctl00_MainContent_btnCheckAll")).click();
		
	
		driver.findElement(By.id("ctl00_MainContent_btnDelete")).click();
		driver.findElement(By.id("ctl00_MainContent_orderLInk")).click();
		driver.navigate().back();
		driver.navigate().back();
		driver.findElement(By.id("ctl00_MainContent_btnUncheckAll")).click();
		driver.findElement(By.id("ctl00_MainContent_orderGrid_ctl02_OrderSelector")).click();
		driver.findElement(By.id("ctl00_MainContent_btnUncheckAll")).click();
	}
	  @Then("^User login should be successful$")  
	  public void User_login_should_be_successful() { if(driver.getTitle().equalsIgnoreCase("Web Orders")){  
	      System.out.println("Test Pass");  
	   } else {  
	      System.out.println("Test Failed");  
	   }  
	 
	   driver.close();  
	   
	}
}
