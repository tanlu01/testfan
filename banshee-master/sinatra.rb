require 'sinatra'

set :bind, '0.0.0.0'
set :port, 8888
set :public_folder, '/tmp/'

before do
  cache_control :no_cache
end

get '/:project' do
  redirect "/#{params[:project]}/docs/html/index.html"
end