package com.lab.api.data;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.lab.api.entity.Comment;
import com.lab.api.vo.CommentsJsonWrapper;
import lombok.RequiredArgsConstructor;
import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;
import org.springframework.stereotype.Component;

import java.io.File;
import java.util.List;

@Component
@RequiredArgsConstructor
public class JsonLoader {

    private final ObjectMapper objectMapper;
    private final ResourceLoader resourceLoader;

    public List<Comment> loadComments(String filePath) throws Exception {
        Resource resource = resourceLoader.getResource("classpath:" + filePath);
        File file = resource.getFile();
        CommentsJsonWrapper wrapper = objectMapper.readValue(file, CommentsJsonWrapper.class);
        return wrapper.getComments().getRow();
    }
}
