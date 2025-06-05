enum Flavor { dev, staging, prod }

class FlavorConfig {
  final Flavor flavor;
  final String apiBaseUrl;
  final String socketUrl;
  final bool enableLog;

  static late FlavorConfig instance;

  FlavorConfig._internal({
    required this.flavor,
    required this.apiBaseUrl,
    required this.socketUrl,
    required this.enableLog,
  });

  factory FlavorConfig({
    required Flavor flavor,
  }) {
    switch (flavor) {
      case Flavor.dev:
        instance = FlavorConfig._internal(
          flavor: flavor,
          apiBaseUrl: 'http://localhost:8000/api/v1',
          socketUrl: 'ws://localhost:8000/api/v1/ws',
          enableLog: true,
        );
        break;
      case Flavor.staging:
        instance = FlavorConfig._internal(
          flavor: flavor,
          apiBaseUrl: 'https://stg.api.zdating.app/api/v1',
          socketUrl: 'wss://stg.api.zdating.app/api/v1/ws',
          enableLog: true,
        );
        break;
      case Flavor.prod:
        instance = FlavorConfig._internal(
          flavor: flavor,
          apiBaseUrl: 'https://api.zdating.app/api/v1',
          socketUrl: 'wss://api.zdating.app/api/v1/ws',
          enableLog: false,
        );
        break;
    }
    return instance;
  }
}
