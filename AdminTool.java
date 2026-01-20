import com.google.auth.oauth2.GoogleCredentials;
import com.google.cloud.firestore.Firestore;
import com.google.firebase.FirebaseApp;
import com.google.firebase.FirebaseOptions;
import com.google.firebase.cloud.FirestoreClient;

import java.io.FileInputStream;
import java.util.HashMap;
import java.util.Map;

public class AdminTool {
    public static void main(String[] args) throws Exception {
        FileInputStream serviceAccount = new FileInputStream("firebase_key.json");

        FirebaseOptions options = new FirebaseOptions.Builder()
                .setCredentials(GoogleCredentials.fromStream(serviceAccount))
                .build();

        FirebaseApp.initializeApp(options);
        Firestore db = FirestoreClient.getFirestore();

        // Template to add a question
        Map<String, Object> data = new HashMap<>();
        data.put("text", "Which programming language is known as the snake?");
        data.put("options", java.util.Arrays.asList("Java", "C++", "Python", "Ruby"));
        data.put("answer", "Python");
        data.put("difficulty", "easy");

        db.collection("questions").add(data);
        System.out.println("Question added successfully!");
    }
}