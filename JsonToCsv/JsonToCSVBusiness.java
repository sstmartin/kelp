
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.net.MalformedURLException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;


public class JsonToCSVBusiness {
 	@SuppressWarnings("unchecked")
    public static void main(String[] args) throws MalformedURLException, IOException {
 		JSONParser parser = new JSONParser();
 		BufferedReader br = new BufferedReader(new FileReader("/home/joey/Documents/yelp/yelp_academic_dataset_business.json"));
 		String line = null;
 		
 		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(
 				new FileOutputStream("/home/joey/Documents/yelp/yelp_academic_dataset_business.bsv")));
 	
 		
 		
 		
 		
 		while ((line = br.readLine()) != null) {
 			Business b = new Business();
        try {
        	
        	JSONObject jsonObject = (JSONObject) parser.parse(line); // Highest level object
 
        	b.business_id = (String) jsonObject.get("business_id");
        	b.full_address = (String) jsonObject.get("full_address");
        	if (b.full_address != null) b.full_address = b.full_address.replace("\n", "\\n");
            b.city = (String) jsonObject.get("city");
            b.state = (String) jsonObject.get("state");
            b.review_count = (long) jsonObject.get("review_count");
            b.name = (String) jsonObject.get("name");
            b.longitude = (double) jsonObject.get("longitude");
            b.latitude = (double) jsonObject.get("latitude");
            b.stars = (double) jsonObject.get("stars");
            b.open = (boolean) jsonObject.get("open");
           
            b.hours = (JSONObject) jsonObject.get("hours");
            b.neighborhoods = (List<String>) jsonObject.get("neighborhoods");
            b.categories = (List<String>) jsonObject.get("categories");
            b.attributes = (JSONObject) jsonObject.get("attributes");
            
        	
        	bw.write(b.toCSV());
        	bw.newLine();
        } catch (Exception e) {
            e.printStackTrace();
        }
 		}
 		br.close();
 		bw.close();
 		System.out.println("Done");
 	}
 	
}
