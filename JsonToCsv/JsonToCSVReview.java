
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


public class JsonToCSVReview {
 	@SuppressWarnings("unchecked")
    public static void main(String[] args) throws MalformedURLException, IOException {
 		JSONParser parser = new JSONParser();
 		BufferedReader br = new BufferedReader(new FileReader("/home/joey/Documents/yelp/yelp_academic_dataset_review.json"));
 		String line = null;
 		
 		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(
 				new FileOutputStream("/home/joey/Documents/yelp/yelp_academic_dataset_review.bsv")));
 	
 		
 		
 		
 		
 		while ((line = br.readLine()) != null) {
 			Review r = new Review();
        try {
        	
        	JSONObject jsonObject = (JSONObject) parser.parse(line); // Highest level object
 
        	r.user_id = (String) jsonObject.get("user_id");
        	r.votes = (JSONObject) jsonObject.get("votes");
        	r.stars = (long) jsonObject.get("stars");
        	r.review_id = (String) jsonObject.get("review_id");
        	r.date = (String) jsonObject.get("date");
        	r.text = (String) jsonObject.get("text");
        	r.type = (String) jsonObject.get("type");
        	r.business_id = (String) jsonObject.get("business_id");
        	
           
            
        	//System.out.println(b.toString());
        	bw.write(r.toCSV());
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
