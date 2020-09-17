package com.skincancerdetection.bffnode.utils;

import com.skincancerdetection.bffnode.BffNodeApplication;
import org.junit.Assert;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest(classes = BffNodeApplication.class)
public class AESEncryptionDecryptionTest {

    @Autowired
    private AESEncryptionDecryption aesEncryptionDecryption;

    @Test
    public void testEncypt() {
        Assert.assertEquals(aesEncryptionDecryption.encrypt("Hello"), "6B8RgW+cQDpBZUrjp5Jz0g==");
    }

    @Test
    public void testDecrypt() {
        Assert.assertEquals(aesEncryptionDecryption.decrypt("6B8RgW+cQDpBZUrjp5Jz0g=="), "Hello");
    }
}
