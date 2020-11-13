import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.File;
import javax.imageio.ImageIO;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.io.*;
import javax.crypto.*;
import javax.crypto.spec.DESKeySpec;
import java.security.*;
import java.awt.image.BufferedImage;

public class GUI extends JFrame implements ActionListener{

	private JButton btnFile, btnEncrypt, btnDecrypt;
	private JLabel lblImg, lblKey, lblMode;
	private JTextField txtKey;
	private JComboBox boxMode;
	private String DES_MODE = "ECB"; //MODO POR DEFAULT
	private static Cipher des;
	private File fileImage;

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
			des = Cipher.getInstance("DES");
		}catch(Exception e){
			System.out.println("ERROR (GUI.main): "+e);
			e.printStackTrace();
		}
	}

	@Override
	public void actionPerformed(ActionEvent e){
		if(e.getSource()==btnFile){
			JFileChooser fileChooser = new JFileChooser();
            fileChooser.setFileFilter(new FileNameExtensionFilter("Images","bmp"));
            int selection = fileChooser.showOpenDialog(this);
            if(selection == JFileChooser.APPROVE_OPTION){
                fileImage = fileChooser.getSelectedFile();
                try{
                    Image image = ImageIO.read(fileImage);
                    lblImg.setText("");
                    lblImg.setIcon(new ImageIcon(image));
                }catch(Exception err){
                    System.out.println("ERROR (GUI.actionPerformed): ");
                    err.printStackTrace();
                }
            }
		}else if(e.getSource()==btnEncrypt){
			String key = txtKey.getText().toString();
			ImageIcon icon = (ImageIcon)lblImg.getIcon();
            BufferedImage buffImage = (BufferedImage)((Image)icon.getImage());
			encryptImage(key,buffImage);
		}else{
			JOptionPane.showMessageDialog(null, "Voy a descifrar papá");
		}
	}

	/*private byte[] getImageHeader(BufferedImage buffImage){
		try{
			ByteArrayOutputStream bout = new ByteArrayOutputStream();
			ImageIO.write(buffImage,"bmp",bout);
			byte[] header = new byte[54];
			byte[] image = bout.toByteArray();
			for(char i=0;i<54;i++){
				header[i] = image[i];
			}
			return header;
		}catch(Exception e){
			System.out.println("ERROR (GUI.getImageHeader): ");
			e.printStackTrace();
			return null;
		}
	}

	private byte[] getImageContent(BufferedImage buffImage){
		try{
			ByteArrayOutputStream bout = new ByteArrayOutputStream();
			ImageIO.write(buffImage,"bmp",bout);
			byte[] image = bout.toByteArray();
			byte[] content = new byte[(image.length - 54)];
			for(char i=54;i<image.length;i++){
				content[i] = image[i];
			}
			return content;
		}catch(Exception e){
			System.out.println("ERROR (GUI.getImageContent): ");
			e.printStackTrace();
			return null;
		}
	}*/

	private void encryptImage(String key,BufferedImage buffImage){
		//DECLARACION DE VARIABLES
		FileInputStream fis;
		FileOutputStream fos;
		CipherInputStream cis;
		int rbytes;
		byte[] bytes = new byte[64]; //DES FUNCIONA CON BLOQUES DE 64 BYTES
		try{
			//PRIMERO SEPARAMOS LA IMAGEN EN CABECERA Y CONTENIDO
			/*byte[] header = getImageHeader(buffImage);
			byte[] content = getImageContent(buffImage);*/
			//CREAMOS UN NUEVO ARCHIVO
			ByteArrayOutputStream bout = new ByteArrayOutputStream();
			ImageIO.write(buffImage,"bmp",bout);
			ByteArrayInputStream image = bout.toByteArray();
			fos = new FileOutputStream(new File("./pruebita.bmp"));
			//LA CABECERA LA VAMOS A ESCRIBIR TAL CUAL EN NUESTRO NUEVO ARCHIVO
			while((rbytes = image.read())<54){ //MIENTRAS NO SE LLEGUE AL FINAL DEL ARCHIVO
				fos.write(image,0,rbytes);
			}
			//COMIENZA PROCESO DE CIFRADO
			//GENERAMOS UNA LLAVE CON LA CLAVE QUE NOS DAN
			SecretKeyFactory factory = SecretKeyFactory.getInstance("DES");
			DESKeySpec keyspec = new DESKeySpec(key.getBytes());
			SecretKey seckey = factory.generateSecret(keyspec);
			des.init(Cipher.ENCRYPT_MODE,seckey);
			byte[] encContent = des.doFinal(image.skip(54));
			while((rbytes = encContent.read())!=-1){ //MIENTRAS NO SE LLEGUE AL FINAL DEL ARCHIVO
				fos.write(encContent,0,rbytes);
			}
			//ESCRIBIMOS LOS BYTES CIFRADOS EN EL ARCHIVO DE SALIDA
			/*fis = new FileInputStream(fileImage);
			cis = new CipherInputStream(fis,des);
			while((rbytes = cis.read(bytes))!=-1){ //MIENTRAS NO SE LLEGUE AL FINAL DEL ARCHIVO
				fos.write(bytes,0,rbytes);
			}*/
			fos.flush();
			fos.close();
			//fis.close();	

		}catch(Exception e){
			System.out.println("ERROR (GUI.encryptImage): ");
			e.printStackTrace();
		}
	}

	private void decryptImage(){

	}

	/*private boolean setImage(BufferedImage image, File file, String ext){
		try{
			file.delete(); //delete resources used by the File
			ImageIO.write(image,ext,file);
			return true;
		}
		catch(Exception e){
			JOptionPane.showMessageDialog(null, "File could not be saved!","Error",JOptionPane.ERROR_MESSAGE);
			e.printStackTrace();
			return false;
		}
	}*/
}