import java.io.File;
import java.io.IOException;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;

public class NegativeImage {
    public static void main(String args[]) throws IOException {
        File f = null;
        BufferedImage img = null;

        // Read image
        try {
            f = new File("input.jpg");
            img = ImageIO.read(f);
        } catch(IOException e) {
            System.out.println(e);
        }

        // Convert to negative
        int width = img.getWidth();
        int height = img.getHeight();
        for( int y=0; y<height; y++ ) {
            for( int x=0; x<width; x++ ) {
                int pixel = img.getRGB(x,y);
                int a = (pixel>>24)&0xff;
                int r = (pixel>>16)&0xff;
                int g = (pixel>>8)&0xff;
                int b = (pixel)&0xff;

                r = 255 - r;
                g = 255 - g;
                b = 255 - b;

                pixel = (a<<24) | (r<<16) | (g<<8) | (b);
                img.setRGB(x,y,pixel);
            }
        }

        // Write image
        try {
            f = new File("output.jpg");
            ImageIO.write(img, "jpg", f);
        } catch(IOException e) {
            System.out.println(e);
        }
    }
}