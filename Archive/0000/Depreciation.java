import java.util.*;  

public class Depreciation{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); 
        System.out.print("Enter a description of the property: ");
        String description = sc.nextLine();
        System.out.print("What is the original value of the equipment? ");
        int beginningValue = sc.nextInt();
        System.out.print("What is the annual depreciation? ");
        int depreciation = sc.nextInt();
        
        System.out.println("Equipment description: " + description);
        System.out.println("Beginning value: " + beginningValue);
        System.out.println("Depreciation: " + depreciation);     
        
        int length = beginningValue/depreciation;
        int endOfYearValue = beginningValue
        int accuDepreciation 
        for (int i = 1; i < length+1; i++) {
            endOfYearValue -= depreciation;
            
        }
        

    }
    
}

