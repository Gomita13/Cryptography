import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.File;
import javax.imageio.ImageIO;
import javax.swing.filechooser.FileNameExtensionFilter;

public class GUI extends JFrame implements ActionListener{

	private JButton btnFile, btnEncrypt, btnDecrypt;
	private JLabel lblImg, lblKey, lblMode;
	private JTextField txtKey;
	private JComboBox boxMode;
	private String DES_MODE = "ECB"; //MODO POR DEFAULT

	public GUI(){
		//INICIALIZANDO LOS COMPONENTES
		lblImg = new JLabel("Your image here",SwingConstants.CENTER);
		lblImg.setBounds(20,10,740,450);
		lblImg.setBackground(new Color(255, 253, 235));
		lblImg.setOpaque(true);

		btnFile = new JButton("Load image");
		btnFile.setBounds(20,490,100,30);
		btnFile.addActionListener(this);

		lblKey = new JLabel("Key: ");
		lblKey.setBounds(150,490,50,30);
		
		txtKey = new JTextField(8); //8 PORQUE LAS CLAVES SON DE 8 BYTES
		txtKey.setBounds(200,490,100,30);

		lblMode = new JLabel("Mode: ");
		lblMode.setBounds(330,490,100,30);

		boxMode = new JComboBox();
		boxMode.setBounds(400,490,100,30);
		boxMode.addItem("ECB");
		boxMode.addItem("CBC");
		boxMode.addItem("CFB");
		boxMode.addItem("OFB");

		btnEncrypt = new JButton("Encrypt");
		btnEncrypt.setBounds(20,550,100,30);
		btnEncrypt.addActionListener(this);

		btnDecrypt = new JButton("Decrypt");
		btnDecrypt.setBounds(200,550,100,30);
		btnDecrypt.addActionListener(this);
		
		//AGREGANDO ELEMENTOS A LA VENTANA
		this.add(lblImg);
		this.add(btnFile);
		this.add(lblKey);
		this.add(txtKey);
		this.add(lblMode);
		this.add(boxMode);
		this.add(btnEncrypt);
		this.add(btnDecrypt);
		//ESPECIFICANDO LA VENTANA
		this.setLayout(null);
		this.setSize(800,660);
		this.setLocationRelativeTo(null);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setVisible(true);
		
	}	

	public static void main(String args[]){
		try{
			new GUI();
		}catch(Exception e){
			System.out.println("ERROR (GUI.main): "+e);
			e.printStackTrace();
		}
	}

	@Override
	public void actionPerformed(ActionEvent e){
		if(e.getSource()==btnFile){
			JFileChooser fileChooser = new JFileChooser();
            fileChooser.setFileFilter(new FileNameExtensionFilter("Images","jpg","png"));
            int selection = fileChooser.showOpenDialog(this);
            if(selection == JFileChooser.APPROVE_OPTION){
                File fileImage = fileChooser.getSelectedFile();
                try{
                    Image image = ImageIO.read(fileImage);
                    lblImg.setText("");
                    lblImg.setIcon(new ImageIcon(image));
                }catch(Exception err){
                    System.out.println("ERROR (Main.actionPerformed): ");
                    err.printStackTrace();
                }
            }
		}else if(e.getSource()==btnEncrypt){
			JOptionPane.showMessageDialog(null, "Voy a cifrar papá");
		}else{
			JOptionPane.showMessageDialog(null, "Voy a descifrar papá");
		}
	}
}