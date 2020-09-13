package com.skincancerdetection.bffnode.controller;

import com.skincancerdetection.bffnode.exception.DuplicateEntryException;
import com.skincancerdetection.bffnode.model.CommonResponse;
import com.skincancerdetection.bffnode.model.RegistrationDto;
import com.skincancerdetection.bffnode.router.CommonServiceRouter;
import org.junit.Assert;
import org.junit.Before;
import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.mockito.Mockito;
import org.mockito.MockitoAnnotations;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.HttpStatus;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
@AutoConfigureMockMvc
public class BffControllerTest {

    @MockBean
    private CommonServiceRouter commonServiceRouter;

    @Autowired
    private BffNodeController controller;

    @Before
    public void setUp() {

        MockitoAnnotations.initMocks(this);

    }

    @Test
    public void testRegisterUser_201() {

        RegistrationDto request = new RegistrationDto();
        request.setUser_id("Shan@gmail.com");
        request.setDob("30-05-1980");
        request.setGender("M");
        request.setPassword("Hello");

        CommonResponse<String> response = new CommonResponse();
        response.setResult("Success");

        Mockito.when(commonServiceRouter.registerUser(request)).thenReturn(response);
        Assert.assertEquals( controller.registerUser(request).getStatusCode().value()
                , HttpStatus.CREATED.value());

    }

    @Test
    public void testRegisterUser_409() {

        RegistrationDto request = new RegistrationDto();
        request.setUser_id("Shan@gmail.com");
        request.setDob("30-05-1980");
        request.setGender("M");
        request.setPassword("Hello");

        DuplicateEntryException entryException = new DuplicateEntryException("HTTP409"
                , "Entry already exists"
                , new RuntimeException());
        try {
            Mockito.when(commonServiceRouter.registerUser(request)).thenThrow(entryException);
        } catch (DuplicateEntryException ex) {
            Assert.assertEquals(ex, entryException);
        }

    }
}
