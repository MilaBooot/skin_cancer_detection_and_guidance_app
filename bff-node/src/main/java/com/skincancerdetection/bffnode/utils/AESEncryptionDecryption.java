package com.skincancerdetection.bffnode.utils;

import com.skincancerdetection.bffnode.enums.ErrorEnum;
import com.skincancerdetection.bffnode.exception.BffNodeException;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import java.util.Base64;

@Component
public class AESEncryptionDecryption {

    @Value("${encryption.secret-key:Winter!$Coming}")
    private String secretKey;

    private static SecretKeySpec secretKeySpec;
    private static byte[] key;
    private static final String ALGORITHM = "AES";

    public void prepareSecreteKey(String myKey) {
        MessageDigest sha = null;
        try {
            key = myKey.getBytes(StandardCharsets.UTF_8);
            sha = MessageDigest.getInstance("SHA-1");
            key = sha.digest(key);
            key = Arrays.copyOf(key, 16);
            secretKeySpec = new SecretKeySpec(key, ALGORITHM);
        } catch (NoSuchAlgorithmException e) {
            throw new BffNodeException(e.getMessage(), e);
        }
    }

    public String encrypt(String strToEncrypt) {
        try {
            prepareSecreteKey(secretKey);
            Cipher cipher = Cipher.getInstance(ALGORITHM);
            cipher.init(Cipher.ENCRYPT_MODE, secretKeySpec);
            return Base64.getEncoder().encodeToString(cipher.doFinal(strToEncrypt.getBytes("UTF-8")));
        } catch (Exception e) {
            throw new BffNodeException(ErrorEnum.ENCRYPTION_ERROR.getErrCode()
                    , ErrorEnum.ENCRYPTION_ERROR.getErrMessage(), e);
        }
    }

    public String decrypt(String strToDecrypt) {
        try {
            prepareSecreteKey(secretKey);
            Cipher cipher = Cipher.getInstance(ALGORITHM);
            cipher.init(Cipher.DECRYPT_MODE, secretKeySpec);
            return new String(cipher.doFinal(Base64.getDecoder().decode(strToDecrypt)));
        } catch (Exception e) {
            throw new BffNodeException(ErrorEnum.DECRYPTION_ERROR.getErrCode()
                    , ErrorEnum.DECRYPTION_ERROR.getErrMessage(), e);
        }
    }


}
