from app.http.handler.notice_lesson import notice_lesson_blueprint
from flask import request, jsonify
from flask_login import login_required
from app.core.controllers import notice_lesson_controller
from app.core.controllers import user_controller
from flask_login import current_user


@notice_lesson_blueprint.route('/notice_lessons')
def find_notice_lessons():
    (notice_lessons, total, err) = notice_lesson_controller.find_notice_lessons(request.args)
    if err is not None:
        return jsonify({
            'code': err.code,
            'message': err.err_info,
            'notice_lessons': None,
            'total': None
        }), err.status_code
    return jsonify({
        'code': 200,
        'total': total,
        'notice_lessons': notice_lessons,
        'message': ''
    }), 200


@notice_lesson_blueprint.route('/notice_lessons', methods=['POST'])
def insert_notice_lesson():
    (ifSuccess, err) = notice_lesson_controller.insert_notice_lesson(request.json)
    if err is not None:
        return jsonify({
            'code': err.code,
            'message': err.err_info,
            'notice_lesson': None,
        }), err.status_code
    return jsonify({
        'code': 200,
        'message': '',
        'notice_lesson': None
    }), 200


@notice_lesson_blueprint.route('/notice_lessons/batch', methods=['POST'])
def insert_notice_lessons():
    (ifSuccess, err) = notice_lesson_controller.insert_notice_lessons(request.json)
    if err is not None:
        return jsonify({
            'code': err.code,
            'message': err.err_info,
            'notice_lesson': None,
        }), err.status_code
    return jsonify({
        'code': 200,
        'message': '',
        'notice_lesson': None
    }), 200


@notice_lesson_blueprint.route('/notice_lessons/<int:id>')
def find_notice_lesson(id):
    (notice_lesson, err) = notice_lesson_controller.find_notice_lesson(id)
    if err is not None:
        return jsonify({
            'code': err.code,
            'message': err.err_info,
            'notice_lesson': None
        }), err.status_code
    return jsonify({
        'code': 200,
        'message': '',
        'notice_lesson': notice_lesson
    }), 200


@notice_lesson_blueprint.route('/notice_lessons/<int:id>', methods=['DELETE'])
def delete_notice_lesson(id):
    (ifSuccess, err) = notice_lesson_controller.delete_notice_lesson(id)
    if err is not None:
        return jsonify({
            'code': err.code,
            'message': err.err_info,
            'notice_lesson': None
        }), err.status_code
    return jsonify({
        'code': 200,
        'message': '',
        'notice_lesson': None
    }), 200


@notice_lesson_blueprint.route('/notice_lessons', methods=['DELETE'])
def delete_notice_lessons():
    (ifSuccess, err) = notice_lesson_controller.delete_notice_lessons(request.json)
    if err is not None:
        return jsonify({
            'code': err.code,
            'message': err.err_info,
            'notice_lesson': None
        }), err.status_code
    return jsonify({
        'code': 200,
        'message': '',
        'notice_lesson': None
    }), 200


@notice_lesson_blueprint.route('/notice_lessons/<int:id>', methods=['PUT'])
def update_notice_lesson(id):
    (ifSuccess, err) = notice_lesson_controller.update_notice_lesson(id, request.json)
    if err is not None:
        return jsonify({
            'code': err.code,
            'message': err.err_info,
            'notice_lesson': None
        }), err.status_code
    return jsonify({
        'code': 200,
        'message': '',
        'notice_lesson': None
    }), 200