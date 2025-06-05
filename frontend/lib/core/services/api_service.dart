import 'dart:async';
import 'package:dio/dio.dart';
import '../config/flavor_config.dart';
import '../storage/storage_service.dart';

class ApiService {
  late final Dio _dio;

  ApiService() {
    final baseOptions = BaseOptions(
      baseUrl: FlavorConfig.instance.apiBaseUrl,
      connectTimeout: const Duration(seconds: 10),
      receiveTimeout: const Duration(seconds: 20),
    );
    _dio = Dio(baseOptions);

    // ── 요청 시 액세스 토큰 헤더 주입
    _dio.interceptors.add(
      InterceptorsWrapper(
        onRequest: (options, handler) async {
          final token = await StorageService.readAccessToken();
          if (token != null) {
            options.headers['Authorization'] = 'Bearer $token';
          }
          handler.next(options);
        },
        // ── 401 발생 시 리프레시 토큰으로 재시도
        onError: (e, handler) async {
          if (e.response?.statusCode == 401) {
            final ok = await _refreshToken();
            if (ok) {
              final retryResponse = await _dio.fetch(e.requestOptions);
              return handler.resolve(retryResponse);
            }
          }
          handler.next(e);
        },
      ),
    );
  }

  // ─────────────────────────────────────────────
  // 내부: 토큰 갱신
  // ─────────────────────────────────────────────
  Future<bool> _refreshToken() async {
    final refresh = await StorageService.readRefreshToken();
    if (refresh == null) return false;

    try {
      final res = await _dio.post(
        '/auth/refresh-token',
        data: {'refresh_token': refresh},
      );

      await StorageService.saveTokens(
        res.data['data']['access_token'] as String,
        res.data['data']['refresh_token'] as String,
      );
      return true;
    } catch (_) {
      await StorageService.clearTokens();
      return false;
    }
  }

  Dio get client => _dio;
}

final apiService = ApiService();
