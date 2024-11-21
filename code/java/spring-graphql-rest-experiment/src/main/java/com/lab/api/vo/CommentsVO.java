package com.lab.api.vo;

import com.lab.api.entity.Comment;
import lombok.Data;

import java.util.List;

@Data
public class CommentsVO {
    List<Comment> row;
}
