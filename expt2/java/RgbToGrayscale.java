import java.io.File;
import java.io.IOException;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;

public class RgbToGrayscale {
    public static void main(String args[]) throws IOException {
        BufferedImage img = null;
        File f = null;

        // Read image
        try {
            f = new File("input.jpg");
            img = ImageIO.read(f);
        } catch(IOException e) {
            System.out.println(e);
        }

        // Convert to grayscale
        int width = img.getWidth();
        int height = img.getHeight();
        for( int y=0; y<height; y++ ) {
            for( int x=0; x<width; x++ ) {
                int pixel = img.getRGB(x,y);
                int a = (pixel>>24)&0xff;
                int b = (pixel>>16)&0xff;
                int g = (pixel>>8)&0xff;
                int r = (pixel)&0xff;

                int avg = (r+b+g)/3;

                pixel =(a<<24) | (avg<<16) | (avg<<8) | avg;
                img.setRGB(x, y, pixel);
            }
        }

        // Save image
        try {
            f = new File("output.jpg");
            ImageIO.write(img, "jpg", f);
        } catch(IOException e) {
            System.out.println(e);
        }
    }
}