import java.util.*;
import javax.swing.JFrame;

public class p3 implements JFrame {
    public static void main(String[] args) {

        JFrame frame = new JFrame("Swing Components Example");

        JLabelnameLabel = new JLabel("Enter your name:");
        nameLabel.setBounds(30, 30, 120, 30);

        JTextFieldnameField = new JTextField();
        nameField.setBounds(160, 30, 150, 30);

        JLabelgenderLabel = new JLabel("Select Gender:");
        genderLabel.setBounds(30, 80, 120, 30);

        JRadioButton male = new JRadioButton("Male");
        male.setBounds(160, 80, 70, 30);
        JRadioButton female = new JRadioButton("Female");
        female.setBounds(230, 80, 80, 30);

        ButtonGroupbg = new ButtonGroup();
        bg.add(male);
        bg.add(female);

        JLabelcourseLabel = new JLabel("Select Course:");
        courseLabel.setBounds(30, 130, 120, 30);

        String[] courses = { "Java", "Python", "C++", "HTML" };
        JComboBox<String> courseBox = new JComboBox<>(courses);
        courseBox.setBounds(160, 130, 150, 30);

        JCheckBox agree = new JCheckBox("I agree to the terms");
        agree.setBounds(30, 180, 200, 30);

        JButtonsubmitBtn = new JButton("Submit");
        submitBtn.setBounds(100, 230, 100, 30);

        JLabel result = new JLabel("");
        result.setBounds(30, 280, 300, 30);

        // Event handling using lambda (no implements or extends)
        submitBtn.addActionListener(e -> {
            if (!agree.isSelected()) {
                result.setText("Please agree to the terms first!");
                return;
            }

            String name = nameField.getText();
            String gender = male.isSelected() ? "Male" : (female.isSelected() ? "Female" : "Not selected");
            String course = (String) courseBox.getSelectedItem();

            result.setText("Hello " + name + " (" + gender + "), Course: " + course);
        });

        frame.add(nameLabel);
        frame.add(nameField);
        frame.add(genderLabel);
        frame.add(male);
        frame.add(female);
        frame.add(courseLabel);
        frame.add(courseBox);
        frame.add(agree);
        frame.add(submitBtn);
        frame.add(result);

        frame.setSize(380, 380);
        frame.setLayout(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}