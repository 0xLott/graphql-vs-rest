package com.lab.api.data;

import com.lab.api.entity.Comment;
import com.lab.api.repository.CommentRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.event.EventListener;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
@Slf4j
@RequiredArgsConstructor
public class DataInitializer {

    private final JsonLoader jsonLoader;
    private final CommentRepository commentRepository;

    @EventListener(ApplicationReadyEvent.class)
    public void loadData() {
        try {
            List<Comment> comments = jsonLoader.loadComments("data.json");
            commentRepository.saveAll(comments);
            log.info("Comments json loaded");
        } catch (Exception e) {
            log.error(e.getMessage(), e);
        }
    }
}