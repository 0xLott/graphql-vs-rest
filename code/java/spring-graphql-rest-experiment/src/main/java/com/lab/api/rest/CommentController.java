package com.lab.api.rest;

import com.lab.api.entity.Comment;
import com.lab.api.repository.CommentRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/rest/comments")
@RequiredArgsConstructor
public class CommentController {

    private final CommentRepository commentRepository;

    /*
- GET /comments: Returns all comments
- GET /comments/:id: Returns a specific comment by id
- GET /comments/user/:id: Returns comments made by specific user id
- GET /comments/min-score/:score: Returns comments with at least the specified score value between 0 and 10
     */

    @GetMapping
    public ResponseEntity<List<Comment>> findAll() {
        return ResponseEntity.ok(commentRepository.findAll());
    }

    @GetMapping("/user/{id}")
    public ResponseEntity<List<Comment>> findByUserId(@PathVariable("id") Long id) {
        return ResponseEntity.ok(commentRepository.findByUserId(id));
    }

    @GetMapping("/min-score/{score}")
    public ResponseEntity<List<Comment>> findByMinScore(@PathVariable("score") Integer score) {
        return ResponseEntity.ok(commentRepository.findByScoreGreaterThanEqual(score));
    }

    @GetMapping("/{id}")
    public ResponseEntity<Comment> findById(@PathVariable("id") Long id) {
        return ResponseEntity.ok(commentRepository.findById(id).orElseThrow());
    }
}
