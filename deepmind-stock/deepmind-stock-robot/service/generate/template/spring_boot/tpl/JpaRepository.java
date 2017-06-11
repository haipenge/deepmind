package ${obj.component.package_name()}.repository.${obj.project.repository};

import ${obj.component.package_name()}.entity.${obj.name};
import com.faceye.feature.repository.jpa.BaseRepository;
/**
 * @说明:${obj.name} 实体Repository
 * @author @haipenge 
 * @Author:haipenge
 * @Create Date:${obj.get_current_date()}
 */
public interface ${obj.name}Repository extends BaseRepository<${obj.name},Long> {
	
	
}
