package Sel;


import org.openqa.selenium.By;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;
import org.openqa.selenium.WebDriver;		
import org.openqa.selenium.chrome.ChromeDriver;	

public class ExcelExampleFile{
@Test(dataProvider="testdata")
public void demoClass(String username, String password) throws InterruptedException {
System.setProperty("webdriver.chrome.driver", "D://eclipse1//Sel_jar//chromedriver_win32//chromedriver.exe");
WebDriver driver = new ChromeDriver();
driver.get("http://secure.smartbearsoftware.com/samples/testcomplete11/WebOrders/login.aspx");
driver.findElement(By.id("ctl00_MainContent_username")).sendKeys("Tester");
driver.findElement(By.name("ctl00$MainContent$password")).sendKeys("test");
driver.findElement(By.className("button")).click();
System.out.println("Login successful");
}

/*@AfterMethod
void ProgramTermination() {
	driver.quit();
} */

@DataProvider(name="testdata")
public Object[][] testDataExample(){
ReadExcelFile configuration = new ReadExcelFile("D://eclipse1//Sel_jar//New XLSX Worksheet.xlsx");
int rows = configuration.getRowCount(0);
Object[][]signin_credentials = new Object[rows][2];

for(int i=0;i<rows;i++)
{
signin_credentials[i][0] = configuration.getData(0, i, 0);
signin_credentials[i][1] = configuration.getData(0, i, 1);
}
return signin_credentials;
}



	}

